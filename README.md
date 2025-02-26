# Document Scanner System

Welcome to the Document Scanner System! This is a simple web application where you can upload text files, compare them for similarity, manage user credits, and view analytics—all with a stylish design. Don’t worry if you’ve never coded before—this guide will explain everything step-by-step, assuming you’re starting from scratch on a Windows computer.

---

## What This Project Does
- **Sign Up & Log In**: Create an account and log in (first user becomes an admin).
- **Credit System**: Get 20 free scans daily; request more if needed (admins approve/deny).
- **Scan Documents**: Upload `.txt` files (costs 1 credit per scan).
- **Find Matches**: See which uploaded files are similar to yours.
- **Analytics**: Admins can see stats like scan counts and credit usage.
- **Look**: A cool design with gradients, glass effects, and teal/orange colors.

---

## What You’ll Need
- **A Windows Computer**: Any recent version (e.g., Windows 10 or 11).
- **Internet**: To download Python and access GitHub.
- **A Web Browser**: Like Chrome, Firefox, or Edge.
- **About 30 Minutes**: To set everything up.

No coding experience? No problem—this guide has you covered!

---

## Step-by-Step Setup Instructions

### 1. Install Python
Python is a programming language we’ll use to run the app.
1. Open your web browser (e.g., Chrome).
2. Go to [python.org/downloads](https://www.python.org/downloads/).
3. Click the big yellow “Download Python 3.x.x” button (e.g., 3.11.5).
4. Run the downloaded file (e.g., `python-3.11.5.exe`).
5. **Important**: Check the box “Add Python to PATH” at the bottom, then click “Install Now”.
6. Wait for it to finish, then close the installer.
7. Open PowerShell:
   - Press `Windows Key + S`, type “PowerShell”, and click it.
8. Test Python:
   - Type `python --version` and press Enter.
   - You should see something like `Python 3.11.5`. If not, restart PowerShell and try again.

### 2. Get the Project Files
You’ll download the project from GitHub, a website where code is shared.
1. In your browser, go to [this project’s GitHub page](#) (replace with the URL after pushing).
2. Click the green “Code” button, then “Download ZIP”.
3. Save the ZIP file somewhere (e.g., Desktop).
4. Right-click the ZIP file, choose “Extract All”, and extract to a folder like `C:\Users\YourName\Desktop\document_scanner`.
5. Open PowerShell:
   - Press `Windows Key + S`, type “PowerShell”, and click it.
6. Move to the project folder:
   - Type `cd C:\Users\YourName\Desktop\document_scanner` (replace `YourName` with your username) and press Enter.
   - Type `dir` to see files like `app.py`, `static/`, `templates/`.

### 3. Set Up a Virtual Environment
This keeps the project’s tools separate from your computer’s other stuff.
1. In PowerShell (in the `document_scanner` folder):
   - Type `python -m venv venv` and press Enter. This creates a `venv/` folder.
2. Activate it:
   - Type `.\venv\Scripts\Activate.ps1` and press Enter.
   - You’ll see `(venv)` before your prompt, like `(venv) PS C:\...`.

### 4. Install Flask
Flask is a tool that makes the web app work.
1. In PowerShell (with `(venv)` active):
   - Type `pip install flask` and press Enter.
   - Wait for it to download and install (takes a minute).
2. Check it worked:
   - Type `pip list` and press Enter.
   - You should see `Flask` listed (e.g., `Flask 2.3.2`).

### 5. Run the App
Now, let’s start the web app!
1. In PowerShell (still in `document_scanner` with `(venv)`):
   - Type `python app.py` and press Enter.
2. You’ll see something like:
Running on http://127.0.0.1:4000

3. Open your browser and type `http://127.0.0.1:5000` in the address bar, then press Enter.
4. You should see the login page with a dark gradient background and a cool form.

### 6. Play with the App
- **Register**: Click “Create an Account”, enter a username (e.g., `testuser`) and password (e.g., `1234`), and sign up. The first user is an admin!
- **Log In**: Use those details to log in.
- **Scan**: Click “Scan Document”, upload a `.txt` file (e.g., create one in Notepad with “Hello world”).
- **Explore**: Try requesting credits, viewing matches, or (as admin) checking the dashboard.

To stop the app, press `Ctrl + C` in PowerShell.

---

## Troubleshooting
- **“python is not recognized”**: Python isn’t in PATH. Reinstall Python and check “Add Python to PATH”.
- **“404” Errors**: Make sure `style.css` is in `static/css/` and templates use `{{ url_for('static', filename='css/style.css') }}`.
- **App Won’t Start**: Type `dir` in PowerShell to check `app.py` is there; restart PowerShell if needed.

---

## Test Data
- Make a few `.txt` files in Notepad:
- `test1.txt`: “This is a test.”
- `test2.txt`: “This is a similar test.”
- Upload them via `/scan` to see matches.

---

## Tech Details (For Curious Beginners)
- **Frontend**: HTML (page structure), CSS (styling), no JavaScript yet.
- **Backend**: Python with Flask (makes the app run).
- **Database**: SQLite (`database.db`) stores users and scans.
- **Files**: Uploaded `.txt` files go to `uploads/`.

---

## Notes
- Change `app.secret_key` in `app.py` to something unique (e.g., `mysecret123`) for security.
- This is a school project—don’t use it online without more security!

Enjoy your Document Scanner System!
