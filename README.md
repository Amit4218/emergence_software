# 🚀 FastAPI Project

A FastAPI backend project with database integration and seed data support.

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- uv (Python package & environment manager)
- Uvicorn

## 🛠 Prerequisites

Make sure you have:

- Python 3.10 or newer
- uv installed

If you don't have uv:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

or via pip:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

## 📥 Clone the Repository

```bash
git clone https://github.com/amit4218/emergence_software.git
cd emergence_software
```

Replace `YOUR_REPO_NAME` with your actual repo name.

## 🏗 Create Virtual Environment

```bash
uv venv
```

Activate it:

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

## 📦 Install Dependencies

```bash
uv sync
```

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL="sqlite:///local.db"
OPENROUTER_API_KEY=""
FRONTEND_BASE_URL="http://localhost:5173"
```

Adjust based on your database (PostgreSQL, MySQL, etc.).

## 🗄 Database Setup

- **SQLite:** Created automatically
- **PostgreSQL:** Create a database manually first

## 🌱 Seed Fake Data

```bash
uv run seed_script.py
```

Expected output: `Fake data seeded successfully!`

## ▶️ Run the Application

```bash
uv run uvicorn main:app --reload
```

Or if inside activated venv:

```bash
uvicorn main:app --reload
```

## Access the App

- API: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🧪 Development Mode

Hot reload is enabled with `--reload`.

## 🧹 Reset Database

If using SQLite:

```bash
rm test.db
```

Then re-run seed script.

## 🚀 Production Run

```bash
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## 🐛 Troubleshooting

**Module not found?**

```bash
source .venv/bin/activate
```

**Database errors?**

- Check your `DATABASE_URL`
- Ensure database server is running
- Verify tables are created before seeding
