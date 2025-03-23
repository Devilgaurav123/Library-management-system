## Library Management System

A web-based **Library Management System** designed for seamless book management, borrowing, and user authentication. Built using **Django, MySQL, HTML, CSS, and JavaScript**, it ensures efficient library operations.

---

## 🚀 Key Features

- **🔐 User Authentication** – Separate login portals for **students** and **admins**
- **📖 Book Management** – Admins can **add, update, delete, and manage books** effortlessly
- **📚 Borrowing & Returning** – Students can **borrow books and return them** within due dates
- **🎨 Responsive UI** – Modern, intuitive, and mobile-friendly design
- **🗄️ MySQL Database Integration** – Secure and efficient data storage
- **⚡ REST API Support** – Complete **CRUD functionality** using **Django REST Framework**

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF), Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **API Support:** Django REST Framework

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/Devilgaurav123/Library-management-system.git
```

### 2️⃣ Navigate to the Project Directory
```sh
cd librarymanagerPro
```

### 3️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Configure MySQL Database
- Create a database named **`library_db`**
- Update **`settings.py`** with your MySQL credentials:
  
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'library_db',
          'USER': 'your_mysql_user',
          'PASSWORD': 'your_mysql_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

### 6️⃣ Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Create an Admin User
```sh
python manage.py createsuperuser
```

### 8️⃣ Run the Development Server
```sh
python manage.py runserver
```

### 9️⃣ Access the Application
```
http://127.0.0.1:8000/
```

---

## 🔥 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/books/` | Retrieve all books |
| `POST` | `/api/books/` | Add a new book |
| `GET` | `/api/books/<id>/` | Retrieve book details |
| `PUT` | `/api/books/<id>/` | Update book details |
| `DELETE` | `/api/books/<id>/` | Delete a book |
| `GET` | `/api/students/` | Retrieve all students |
| `POST` | `/api/students/` | Add a new student |
| `GET` | `/api/borrowed-books/` | Retrieve borrowed books |
| `POST` | `/api/borrowed-books/` | Borrow a book |
| `PUT` | `/api/borrowed-books/<id>/` | Update book return status |
| `DELETE` | `/api/borrowed-books/<id>/` | Delete a borrowed book record |

---

## 🏆 Unique Admin Feature

### 📊 **Admin Dashboard Enhancements**

- **📅 Due Date Tracker** – View a **list of overdue books** in one glance
- **📌 Quick Actions** – **Approve/Deny** book requests directly from the dashboard
- **📜 Activity Logs** – Track **all transactions** (borrowed, returned, and deleted books)
- **📢 Notifications** – Notify students about **due dates and late fees**

---

## 🎯 Future Enhancements

- **📌 Pagination** – Add **pagination** for book listings
- **🔑 JWT Authentication** – Enhance security with **JSON Web Tokens**
- **📅 Return Date Tracking** – Implement an **automated fine system** for late returns

---

## 🛠 Contribution Guide

Interested in contributing? Follow these steps:

- **Fork** the repository
- Create a **new feature branch**
- Make changes and **commit** with meaningful messages
- Submit a **Pull Request (PR)**

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify as needed.

---

