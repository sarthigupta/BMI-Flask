BMI Calculator (Flask)

A beginner-friendly BMI (Body Mass Index) Calculator built using Flask.
This project includes basic authentication and BMI calculation functionality. It was created for learning Flask fundamentals, routing, templates, form handling, and authentication flow.

Features
User Login Authentication (Simple)
BMI Calculation
User Input Form
BMI Category Detection
Flask Routing
HTML Templates Rendering
Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS
Authentication: Variable-based authentication (No Database)
Project Purpose

This project was built as a learning project to understand the basics of Flask development.

The authentication system is implemented using simple variables instead of a database, as the main focus was learning:

Flask Routing
Request Handling
Template Rendering
Form Submission
Basic Authentication Logic
Project Structure
BMI-Calculator/
│── app.py
│── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── register.html
│── static/
│── requirements.txt
│── README.md
Installation
1. Clone the Repository
git clone <your-repository-link>
cd BMI-Calculator
2. Create Virtual Environment
python -m venv .venv
3. Activate Virtual Environment

Windows

.venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Run the Flask App
python app.py