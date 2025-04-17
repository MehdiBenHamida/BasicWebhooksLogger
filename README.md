# 🚀 FastAPI Webhook Logger

A modern webhook logging system built with **FastAPI**, **SQLite**, **SQLAlchemy**, **Bootstrap 5**, and **Jinja2**.  
It receives webhook requests, logs them to a database, displays them in a responsive web UI, and provides an API endpoint to fetch the logs.

---

## 📦 Features

- ✅ Log all POST requests to `/webhooks` (headers, payload, etc.)
- ✅ Store logs in a SQLite database using SQLAlchemy ORM
- ✅ View logs in a modern Bootstrap UI with:
  - DataTables integration (search, sort, pagination, fixed header)
  - Scrollable long fields
  - Pretty-printed JSON payloads
  - Bulk or single delete
- ✅ REST API endpoint to retrieve all logs (`GET /api/logs`)
- ✅ Clean, modular codebase with separation of concerns

---

## 🛠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- [DataTables](https://datatables.net/)
- [Jinja2](https://jinja.palletsprojects.com/)

---

## 🚀 Getting Started

### 📋 Requirements

- Python 3.8+
- pip

---

### 🔧 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/webhook-logger.git
cd webhook-logger

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
