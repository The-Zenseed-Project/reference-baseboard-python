# 🐣 Getting Started with the Zenseed Baseboard (Python)

This guide walks you through every step to get your Zenseed-compatible baseboard running — **no prior experience required**.

---

## ✅ What You Need

- A computer with internet access
- [Git](https://git-scm.com/downloads) installed
- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop) (optional but recommended)

---

## 📦 Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/The-Zenseed-Project/reference-baseboard-python.git
cd reference-baseboard-python
```

---

## 🐍 Step 2: Set Up a Python Environment

If not using Docker:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Step 3: Run the App

### With Python directly:

```bash
uvicorn app.main:app --reload
```

Then visit [http://localhost:8000](http://localhost:8000)

---

### Or with Docker:

```bash
docker-compose up --build
```

---

## 🔎 Step 4: Test It

Open your browser and try:

- [http://localhost:8000/meta](http://localhost:8000/meta) – Metadata and module list
- [http://localhost:8000/modules](http://localhost:8000/modules) – Loaded module implementations
- [http://localhost:8000/i18n](http://localhost:8000/i18n) – Language scaffolding
- [http://localhost:8000/accessibility](http://localhost:8000/accessibility) – UI accessibility options

---

## 🧩 Step 5: Explore Modular Design

The file `modules.yaml` defines which modules are used. You can swap any component (e.g. `auth`, `secrets`, `rbac`) by changing this file and ensuring the correct implementation exists.

Each module follows an interface like `auth_interface.py` for clean separation.

---

## 📚 Learn More

For full documentation on how Zenseed modules work, contributing standards, and ethical principles, see:

👉 [Zenseed Docs on GitHub](https://github.com/The-Zenseed-Project/docs)

---

## 🤝 Need Help?

You can ask questions and get support by:
- Raising an issue in this repo
- Joining the Zenseed community (coming soon)

---

Happy hacking 🌱
