💰 Expense Tracker Web Application

A simple Flask-based expense tracking web application that allows users to:

Register and login securely

Add, view, and categorize expenses

Monitor their spending with insightful dashboards

Set category-wise budget limits and receive alerts

🚀 Features

🔐 User Authentication (Register/Login/Logout)

💸 Add and manage expenses with categories

📊 Dashboard with pie chart visualization (Plotly)

⚠️ Budget alert system

📆 Timestamped expense entries

🧼 Responsive UI built with Bootstrap 5

🛠️ Tech Stack

Backend: Flask, SQLAlchemy, Flask-Login

Frontend: HTML5, CSS3, Bootstrap 5

Database: SQLite

Charts: Plotly.js

📂 Project Structure

expense_tracker/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── utils.py               # Business logic (insights, alerts)
├── templates/             # HTML templates (Jinja2)
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── dashboard.html
├── static/                # Static files (CSS/JS)
│   └── style.css
├── expenses.db            # SQLite database file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

⚙️ Installation

1. Clone the repository

git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

2. Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

Go to http://127.0.0.1:5000 in your browser.

📌 Default Routes

Route

Description

/

Main page (requires login)

/login

Login form

/register

Registration form

/add

Add new expense

/dashboard

View summary + budget alerts

/logout

Logout current user

📈 Dashboard Insights

View total and category-wise spending

Visualized with a pie chart (Plotly.js)

Get warning alerts if you exceed your set budget

📦 Dependencies

Flask
Flask-Login
Flask-SQLAlchemy
Werkzeug
pandas

Install them via:

pip install -r requirements.txt

✅ Future Improvements

Edit/Delete individual expenses

Export to CSV or PDF

Monthly budget tracking

Mobile-first design

Add dark mode 🌙

🤝 Contributing

Pull requests are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a PR.

📄 License

MIT License. Feel free to use and modify.

✨ Author

Omkar Narveer

Happy Tracking 💰!

