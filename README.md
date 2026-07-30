# loginSystem
# 🎓 Django Student Registration & Login System

A simple and secure **Student Registration & Login System** built using **Django**. This project demonstrates user authentication using Django's built-in authentication system while storing additional student details in a custom `Student` model.

---

## 🚀 Features

- 🏠 Home Page
- 👤 Student Registration
- 🔐 Secure Login
- 🚪 Logout
- 📊 Dashboard (Login Required)
- ✅ Password Confirmation Validation
- 📧 Duplicate Email Validation
- 💬 Django Messages Framework
- 🔒 Authentication using Django's built-in `User` model
- 🎨 Responsive Bootstrap 5 UI

---

## 🛠️ Technologies Used

- Python 3.x
- Django
- SQLite3
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

---

## 📁 Project Structure

```
PracticeProjectDjango/
│
├── app2/
│   ├── migrations/
│   ├── templates/
│   │   └── app2/
│   │       ├── index.html
│   │       ├── signup.html
│   │       ├── login.html
│   │       └── dashboard.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── practiceproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/
├── static/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/student-login-system.git
```

### Navigate to the project

```bash
cd student-login-system
```

### Create a virtual environment

#### Windows (CMD)

```cmd
python -m venv .venv
```

Activate the virtual environment

```cmd
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📸 Pages

- Home
- Sign Up
- Sign In
- Dashboard
- Logout

---

## 🔐 Authentication Flow

1. User registers.
2. Django creates a `User` account.
3. Student information is stored in the `Student` model.
4. User signs in using email and password.
5. Django authenticates the user.
6. Logged-in users are redirected to the dashboard.
7. Logout destroys the session.

---

## 📂 Student Model

Stores additional student information such as:

- Name
- Email
- Mobile Number
- Date of Birth
- City

---

## 📚 Learning Objectives

This project demonstrates:

- Django Models
- Django Views
- URL Routing
- HTML Forms
- Bootstrap Integration
- Django Authentication
- Login & Logout
- Form Validation
- Django Messages Framework
- Login Required Decorator

---

## 🚀 Future Improvements

- Password Reset
- Email Verification
- User Profile
- Edit Profile
- Change Password
- Profile Picture Upload
- Search Students
- Admin Dashboard
- Pagination
- REST API
- JWT Authentication

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## 📄 License

This project is created for learning purposes and is free to use.

---

## ⭐ If you found this project helpful

Please give this repository a ⭐ on GitHub.
