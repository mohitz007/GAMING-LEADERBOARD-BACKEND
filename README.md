
````markdown
# 🕹️ Gaming Leaderboard Backend (Django)

This is a **Django-based backend** designed for a gaming leaderboard system. It tracks player scores, ranks them accordingly, and provides an admin interface to manage game data. Built with simplicity in mind, it uses SQLite by default and is easily extensible.

---

## 🚀 Features

- Player registration and management  
- Score submission and leaderboard ranking  
- Admin dashboard (via Django Admin)  
- Seed data support  
- Lightweight setup with SQLite  
- Optional New Relic integration for performance monitoring

---

## 🧰 Tech Stack

- **Framework**: Django (Python)
- **Database**: SQLite (default)
- **Performance Monitoring**: New Relic (optional)
- **Language**: Python 3.x

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mohitz007/GAMING-LEADERBOARD-BACKEND.git
cd GAMING-LEADERBOARD-BACKEND/mohit
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuration

If using New Relic, you can configure it via the `newrelic.ini` file. Otherwise, this step can be skipped.

---

## 🧪 Run the Project Locally

### Apply Migrations

```bash
python manage.py migrate
```

### (Optional) Load Seed Data

```bash
sqlite3 db.sqlite3 < seed_data.sql
```

### Start the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Admin Access

To access Django's admin panel:

### Create Superuser

```bash
python manage.py createsuperuser
```

Then go to: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📁 Folder Structure

```
mohit/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── seed_data.sql
├── newrelic.ini
├── [leaderboard]
```

---

## 🙌 Contributions

Open to contributions! If you find a bug or have a feature request, feel free to open an issue or submit a PR.

---
