# Document Scanner System

Welcome to the Document Scanner System! This is a web application where you can sign up, scan text files to find similarities, manage credits, and (for admins) view detailed analytics—all with a sleek, modern design. This guide assumes you’re new to coding and uses Windows with PowerShell, walking you through setup from scratch.

---

## What This Project Does
- **Sign Up & Log In**: Create an account or log in (first user is an admin).
- **Credit System**: Get 20 free scans daily; request more credits if needed (admins approve/deny inline).
- **Scan Documents**: Upload `.txt` files (1 credit per scan) and see matches instantly.
- **Analytics Dashboard**: Admins can view stats (scans per user, top credits, request statuses) on a dedicated page.
- **Design**: Gradient backgrounds, glassmorphism, teal/orange accents, and inline messages for a smooth experience.

---

## What You’ll Need
- **A Windows Computer**: Windows 10 or 11 works fine.
- **Internet**: To download tools and access GitHub.
- **A Web Browser**: Chrome, Firefox, or Edge.
- **30-45 Minutes**: For setup and exploration.

No prior coding knowledge required—I’ve got you covered!

---

## Step-by-Step Setup Instructions

### 1. Install Python
Python runs the app.
1. Open your browser (e.g., Chrome).
2. Go to [python.org/downloads](https://www.python.org/downloads/).
3. Click “Download Python 3.x.x” (e.g., 3.11.5).
4. Run the installer:
   - Check “Add Python to PATH” at the bottom.
   - Click “Install Now”, then “Close” when done.
5. Open PowerShell:
   - Press `Windows Key + S`, type “PowerShell”, hit Enter.
6. Test it:
   - Type `python --version` and press Enter.
   - See `Python 3.11.5` (or similar)? You’re good! If not, restart PowerShell and retry.

### 2. Get the Project Files
Download the code from GitHub.
1. In your browser, go to [this project’s GitHub page](#) (replace with your URL after pushing).
2. Click the green “Code” button → “Download ZIP”.
3. Save it (e.g., to Desktop), then right-click → “Extract All” → extract to `C:\Users\YourName\Desktop\document_scanner`.
4. In PowerShell:
   - Type `cd C:\Users\YourName\Desktop\document_scanner` (use your username) and press Enter.
   - Type `dir` to see files like `app.py`, `static/`, `templates/`.

### 3. Set Up a Virtual Environment
This keeps the app’s tools separate.
1. In PowerShell (in `document_scanner`):
   - Type `python -m venv venv` and press Enter. You’ll see a `venv/` folder.
2. Activate it:
   - Type `.\venv\Scripts\Activate.ps1` and press Enter.
   - See `(venv)` in the prompt? It’s active!

### 4. Install Flask
Flask makes the web app work.
1. In PowerShell (with `(venv)`):
   - Type `pip install flask` and press Enter. Wait for it to finish.
2. Verify:
   - Type `pip list`—you’ll see `Flask` (e.g., `2.3.2`).

### 5. Run the App
Start the web app!
1. In PowerShell:
   - Type `python app.py` and press Enter.
   - See `* Running on http://127.0.0.1:5000`? It’s working!
2. Open your browser, go to `http://127.0.0.1:5000`.
3. You’ll see a login page with a dark gradient and cool design.

### 6. Use the App
- **Register**: Click “Sign Up”, enter a username (e.g., `testuser`) and password (e.g., `1234`). First user is admin!
- **Log In**: Use those details—see “Login successful!” and your profile.
- **Scan**: Upload a `.txt` file (e.g., “Hello world” in Notepad), see matches inline.
- **Request Credits**: Enter a number, click “Request Credits”, see “Credit request sent!”.
- **Admin Features**: As admin, approve/deny requests inline, or click “Analytics Dashboard” for stats.
- **Logout**: Click “Logout”, see “Logout successful!”, return to login.

Stop the app with `Ctrl + C` in PowerShell.

---

## Troubleshooting
- **“python is not recognized”**: Reinstall Python with “Add to PATH” checked.
- **No Styling**: Ensure `static/css/style.css` exists; clear browser cache (`Ctrl + Shift + Delete`).
- **“403 Unauthorized”**: Log in as admin to access analytics.

---

## Test Data
- Create `.txt` files in Notepad:
  - `test1.txt`: “This is a test.”
  - `test2.txt`: “This is a similar test.”
- Upload via “Scan a Document” to test matching.

---

## Tech Details
- **Frontend**: HTML (`index.html` for main app, `dashboard.html` for analytics), CSS (styling), JavaScript (dynamic updates in `script.js`).
- **Backend**: Python with Flask (`app.py`).
- **Database**: SQLite (`database.db`) for users, scans, and requests.
- **Files**: Uploaded `.txt` files saved in `uploads/`.

---

## Notes
- Change `app.secret_key` in `app.py` to something unique (e.g., `mysecretkey`) for security.
- This is a local project—runs on your computer, not online.

Enjoy exploring the Document Scanner System!