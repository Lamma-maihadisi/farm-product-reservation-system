# 🐓 Farm Reservation System

This is an enhanced **Farm Product Reservation System** that allows customers to reserve poultry and egg products online.  
The system also sends **automated confirmation emails** after a successful reservation, improving trust and communication.  

---

## ✨ Features
- 🐔 Reserve poultry and eggs online  
- 📧 Receive automated confirmation email after booking  
- 📊 Admin panel for managing reservations and products  
- 📱 Mobile responsive design  
- 🔒 Secure and simple system (future enhancement: payment integration)  

---

## ⚙️ Technologies Used
- **Backend:** Django (Python)  
- **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Email Service:** Django Email (SMTP setup required)  
- **Version Control:** Git & GitHub  

---

## 📦 Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YourUsername/farm-reservation-system.git
cd farm-reservation-system
```

### 2️⃣ Create Virtual Environment (Pipenv)
```bash
pip install pipenv
pipenv install
pipenv shell
```

Or using venv:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Superuser (for Admin Access)
```bash
python manage.py createsuperuser
```

### 5️⃣ Run Development Server
```bash
python manage.py runserver
```

Go to 👉 http://127.0.0.1:8000

---

## 📧 Email Setup (For Confirmation Emails)

In `settings.py`, configure your email backend (example with Gmail):  

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # use App Password, not normal password
```

---

## 🗂 Project Structure
```
farm-reservation-system/
│── farm/                # Django app
│── templates/           # HTML templates
│── static/              # CSS, JS, images
│── db.sqlite3           # Database
│── manage.py            # Django manager
│── requirements.txt     # Dependencies
```

---

## 🚀 Future Enhancements
- 💳 Online payment integration  
- 👤 User authentication (login, profiles)  
- 📱 SMS notifications for reservations  

---

## 👨‍💻 Author
Muhammad Umar  
Undergraduate Project – Kaduna State University  
