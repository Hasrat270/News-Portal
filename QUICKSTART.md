# Quickstart Guide

All commands must be executed from the project root directory:
`/home/hasrat/Documents/News-Portal`

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```
   *(Note: If the virtual environment is broken, recreate it using: `python3 -m venv venv && source venv/bin/activate && pip install django pillow`)*

2. **Run Migrations:**
   ```bash
   python3 manage.py migrate
   ```

3. **Start Development Server:**
   ```bash
   python3 manage.py runserver
   ```

4. **Stop Development Server:**
   Press `Ctrl + C` in the terminal where the server is running.
