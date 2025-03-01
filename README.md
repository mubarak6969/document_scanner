# Document Scanner System

Welcome to the Document Scanner System! This is a web application where you can sign up, scan text files to find similarities, manage credits, and (for admins) view analytics and manage roles—all with a professional, responsive design that fits all devices without scrolling.

----

This repository includes:
1. **README.md**: Setup instructions (below).
2. **Code Files**:
   - **Frontend**: `templates/index.html` (main app), `templates/dashboard.html` (analytics), `static/css/style.css` (styling), `static/js/script.js` (client-side logic).
   - **Backend**: `app.py` (Flask app).
   - **Database**: `database.db` (SQLite, created on first run).
3. **Test Data**: Sample documents in `uploads/` for testing similarity matching.

---

## What This Project Does
- **Sign Up & Log In**: Create an account or log in (first user is an admin).
- **Credit System**: 20 free scans daily; request more credits if needed (admins approve/deny).
- **Scan Documents**: Upload `.txt` files (1 credit per scan) and see matches instantly.
- **Admin Features**: Approve/deny credits, change user roles, view analytics (scans, credits, requests).
- **Design**: Professional, centered layout with navy blue accents, fits all devices without scrolling.

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
Download the code from this GitHub repository.
1. In your browser, go to [this project’s GitHub page](https://github.com/yourusername/document-scanner) (replace with your repo URL).
2. Click the green “Code” button → “Download ZIP”.
3. Save it (e.g., to Desktop), then right-click → “Extract All” → extract to `C:\Users\YourName\Desktop\document_scanner`.
4. In PowerShell:
   - Type `cd C:\Users\YourName\Desktop\document_scanner` (use your username) and press Enter.
   - Type `dir` to see files like `app.py`, `static/`, `templates/`, `uploads/`.

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
3. You’ll see a login page with a centered, professional design.

### 6. Use the App
- **Register**: Click “Sign Up”, enter a username (e.g., `testuser`) and password (e.g., `1234`). First user is admin!
- **Log In**: Use those details—see “Login successful!” and your profile.
- **Scan**: Use test data in `uploads/` or upload new `.txt` files (e.g., “Hello world”), see matches.
- **Request Credits**: Enter a number, click “Request Credits”, see “Credit request sent!”.
- **Admin Features**: As admin, approve/deny credits, change user roles (e.g., make `testuser` an admin), view analytics.
- **Logout**: Click “Logout”, return to login.

Stop the app with `Ctrl + C` in PowerShell.

---

## Test Data
The `uploads/` folder contains predefined test documents to try the similarity matching feature:
- `test1.txt`: "This is a test document for checking similarity."
- `test2.txt`: "This is a similar test document for checking." (similar to test1.txt for matching).
- `test3.txt`: "Completely different content for testing." (different to show no match).

### How to Use Test Data
1. Log in as a user (e.g., `testuser`).
2. Go to "Scan a Document", upload `test1.txt`, then `test2.txt` → See high similarity match (due to Levenshtein distance).
3. Upload `test3.txt` → See no match (below 70% similarity).

---

## Troubleshooting
- **“python is not recognized”**: Reinstall Python with “Add to PATH” checked.
- **No Styling**: Ensure `static/css/style.css` exists; clear browser cache (`Ctrl + Shift + Delete`).
- **“403 Unauthorized”**: Log in as admin to access analytics/role management.
- **JavaScript Errors**: Check browser console (`F12`), ensure `static/js/script.js` exists.

---

## Code Files Overview
- **Frontend**:
  - `templates/index.html`: Main app (login, signup, profile, scans, credits, admin features).
  - `templates/dashboard.html`: Admin analytics dashboard.
  - `static/css/style.css`: Professional styling, centered, fits all devices without scrolling.
  - `static/js/script.js`: Client-side logic (switching, form submissions, role changes).
- **Backend**:
  - `app.py`: Flask app handling routes, logic, and database.
- **Database**:
  - `database.db`: SQLite database (created on first run) for users, documents, credit requests.

---

## Notes
- Change `app.secret_key` in `app.py` to something unique for security.
- This is a local project—runs on your computer, not online.
- Test on different devices (desktop, tablet, mobile) to verify responsive design.

Enjoy exploring the Document Scanner System!