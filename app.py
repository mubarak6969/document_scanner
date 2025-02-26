from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
from datetime import datetime
import hashlib

app = Flask(__name__)
app.secret_key = 'super-secret-key-123'  # Change this to a unique, secure key
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize SQLite database with required tables
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Users table: stores user info
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user',
        credits INTEGER DEFAULT 20,
        last_reset TEXT
    )''')
    # Documents table: stores uploaded documents
    c.execute('''CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        content TEXT,
        upload_date TEXT
    )''')
    # Credit requests table: stores requests for additional credits
    c.execute('''CREATE TABLE IF NOT EXISTS credit_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        requested_credits INTEGER,
        status TEXT DEFAULT 'pending'
    )''')
    conn.commit()
    conn.close()

# Reset all users' credits to 20 daily
def reset_credits():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT id, last_reset FROM users")
    users = c.fetchall()
    today = datetime.now().strftime('%Y-%m-%d')
    for user in users:
        last_reset = user[1] or '1970-01-01'
        if last_reset != today:
            c.execute("UPDATE users SET credits = 20, last_reset = ? WHERE id = ?", (today, user[0]))
    conn.commit()
    conn.close()

# Run credit reset before each request
@app.before_request
def before_request():
    reset_credits()

# Calculate Levenshtein distance for text similarity
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

# Root route: redirect to profile or login
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('profile'))
    return redirect(url_for('login'))

# User registration
@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        try:
            role = 'admin' if c.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0 else 'user'
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Username already exists"
        finally:
            conn.close()
    return render_template('register.html')

# User login
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            session['role'] = user[3]
            return redirect(url_for('profile'))
        return "Invalid credentials"
    return render_template('login.html')

# User profile page
@app.route('/user/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT username, credits, role FROM users WHERE username = ?", (session['username'],))
    user = c.fetchone()
    c.execute("SELECT filename, upload_date FROM documents WHERE user_id = (SELECT id FROM users WHERE username = ?)", (session['username'],))
    scans = c.fetchall()
    conn.close()
    return render_template('profile.html', username=user[0], credits=user[1], role=user[2], scans=scans)

# Request additional credits
@app.route('/credits/request', methods=['GET', 'POST'])
def request_credits():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        credits = int(request.form['credits'])
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO credit_requests (user_id, requested_credits) VALUES ((SELECT id FROM users WHERE username = ?), ?)", 
                  (session['username'], credits))
        conn.commit()
        conn.close()
        return "Credit request submitted successfully"
    return render_template('request_credits.html')

# Admin credit management
@app.route('/admin/credits', methods=['GET', 'POST'])
def admin_credits():
    if 'role' not in session or session['role'] != 'admin':
        return "Unauthorized"
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if request.method == 'POST':
        request_id = request.form['request_id']
        action = request.form['action']
        c.execute("SELECT user_id, requested_credits FROM credit_requests WHERE id = ?", (request_id,))
        req = c.fetchone()
        if action == 'approve':
            c.execute("UPDATE users SET credits = credits + ? WHERE id = ?", (req[1], req[0]))
            c.execute("UPDATE credit_requests SET status = 'approved' WHERE id = ?", (request_id,))
        else:
            c.execute("UPDATE credit_requests SET status = 'denied' WHERE id = ?", (request_id,))
        conn.commit()
    c.execute("SELECT cr.id, u.username, cr.requested_credits, cr.status FROM credit_requests cr JOIN users u ON cr.user_id = u.id")
    requests = c.fetchall()
    conn.close()
    return render_template('admin.html', requests=requests)

# Document upload and scanning
@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT credits FROM users WHERE username = ?", (session['username'],))
    credits = c.fetchone()[0]
    if credits <= 0:
        conn.close()
        return "No credits available. Request more or wait for the daily reset."
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            c.execute("INSERT INTO documents (user_id, filename, content, upload_date) VALUES ((SELECT id FROM users WHERE username = ?), ?, ?, ?)", 
                      (session['username'], filename, content, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            c.execute("UPDATE users SET credits = credits - 1 WHERE username = ?", (session['username'],))
            conn.commit()
            doc_id = c.lastrowid
            conn.close()
            return redirect(url_for('matches', doc_id=doc_id))
        conn.close()
        return "Please upload a .txt file"
    conn.close()
    return render_template('scan.html')

# Find matching documents
@app.route('/matches/<int:doc_id>')
def matches(doc_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT content FROM documents WHERE id = ?", (doc_id,))
    target_content = c.fetchone()
    if not target_content:
        conn.close()
        return "Document not found"
    target_content = target_content[0]
    c.execute("SELECT id, filename, content FROM documents WHERE id != ?", (doc_id,))
    all_docs = c.fetchall()
    matches = []
    for doc in all_docs:
        distance = levenshtein_distance(target_content, doc[2])
        similarity = 1 - (distance / max(len(target_content), len(doc[2])))
        if similarity > 0.7:  # 70% similarity threshold
            matches.append({'id': doc[0], 'filename': doc[1], 'similarity': similarity * 100})
    matches.sort(key=lambda x: x['similarity'], reverse=True)
    conn.close()
    return render_template('matches.html', matches=matches)

# Admin analytics dashboard
@app.route('/admin/analytics')
def analytics():
    if 'role' not in session or session['role'] != 'admin':
        return "Unauthorized"
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT u.username, COUNT(d.id) as scans FROM users u LEFT JOIN documents d ON u.id = d.user_id GROUP BY u.id, u.username")
    scan_stats = c.fetchall()
    c.execute("SELECT username, credits FROM users ORDER BY credits DESC LIMIT 5")
    top_users = c.fetchall()
    c.execute("SELECT status, COUNT(*) FROM credit_requests GROUP BY status")
    credit_stats = c.fetchall()
    conn.close()
    return render_template('dashboard.html', scan_stats=scan_stats, top_users=top_users, credit_stats=credit_stats)

# Logout user
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)