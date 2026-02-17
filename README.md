# 📚 Student Study Portal

A full-stack web application built with **Django** that helps students manage their academic activities through a centralized, interactive dashboard. The platform combines productivity tools, learning resources, and academic utilities into a single system — reducing the need to juggle multiple disconnected apps.

---

## 🚀 Features

### 🔐 Authentication
- Secure signup, login, and logout
- Username & email uniqueness validation
- Session-based authentication
- Protected routes via Django login decorators

### 📝 Notes Management
- Create and save personal study notes
- View note list and individual note detail
- Delete notes

### 📘 Homework Tracker
- Add homework tasks with due dates
- Mark tasks as completed or pending
- Delete entries
- Progress tracking overview

### ✅ To-Do List
- Create and manage daily tasks
- Toggle task completion status
- Delete tasks
- Productivity tracking

### 📺 YouTube Study Search
- Search educational videos directly within the portal
- Displays title, description, channel, duration, published date, and thumbnail
- Powered by [`scrapetube`](https://github.com/dermasmid/scrapetube)

### 📚 Book Search
- Search books by keyword via the **Google Books API**
- Displays title, authors, description, categories, ratings, page count, and a preview link

### 📖 Dictionary Tool
- Look up word definitions, pronunciation (with audio), example sentences, and synonyms
- Powered by the [Dictionary API](https://dictionaryapi.dev/)

### 🌐 Wikipedia Search
- Search and browse Wikipedia article summaries
- Direct links to full articles via the Wikipedia API

### 🔁 Unit Converter
- Kilometer ↔ Meter
- Celsius ↔ Fahrenheit

### 👤 Profile Dashboard
- Personalized user dashboard
- At-a-glance view of homework, to-do tasks, and completion status

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django (Python) |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite |
| APIs | Google Books API, Wikipedia API, Dictionary API |
| External Library | scrapetube |
| Authentication | Django built-in auth |

---

## 🗂️ Project Structure

```
Student Study Portal/
│
├── account/                    # User authentication app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── dashboard/                  # Core features app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── forms.py
│   └── models.py
│
├── studentstudyportal/         # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── media/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BikashGosain/Student-Study-Portal.git
cd student-study-portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Activate — Linux / macOS
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser *(optional)*

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎯 Project Objectives

- Provide a **centralized academic productivity platform** for students
- Reduce dependency on multiple disconnected learning tools
- Improve **task organization and time management**
- Combine learning, productivity, and organization into one unified system

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

*Built with ❤️ using Django*
