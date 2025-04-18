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
```

### 🌍 Expose Webhook Endpoint with Ngrok

If you're testing webhooks from third-party services (like Stripe, GitHub, etc.), you'll need a public URL that tunnels to your local server. That's where Ngrok comes in.

#### 🔧 Install Ngrok

If you don’t have Ngrok installed:

```bash
# Mac (Homebrew)
brew install ngrok/ngrok/ngrok

# Debian / Ubuntu
sudo snap install ngrok

# Or download manually:
https://ngrok.com/download
```

Then login to link your Ngrok account (once):

```bash
ngrok config add-authtoken <your-token>
```

#### ▶️ Run your FastAPI app

Start your FastAPI app locally:

```bash
uvicorn app.main:app --reload
```
By default, it listens on: http://localhost:8000

#### 🌐 Start Ngrok Tunnel

In a separate terminal, run:

```bash
ngrok http 8000
```

Ngrok will output something like:

```
Forwarding    https://e2a5-84-71-123-45.ngrok-free.app -> http://localhost:8000
```

Copy the generated HTTPS URL — that is your public webhook gateway.


#### 📩 Use the Public URL in Webhooks

Update your external webhook provider to send POST requests to: 
`https://your-ngrok-subdomain.ngrok-free.app/webhooks`
Ngrok will tunnel those requests directly to your local FastAPI app at /webhooks.

