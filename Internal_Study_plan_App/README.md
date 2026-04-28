# 90-Day GenAI Internal Study Plan Application

This application is a specialized tracker for the 10-stage Generative AI Roadmap. It helps monitor progress through a 90-day structured learning path, featuring a FastAPI backend and a premium React frontend.

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites
- **Python 3.10+**
- **Node.js (v18 or higher)**
- **npm** (usually comes with Node.js)

---

## 🛠️ Backend Setup (FastAPI)

The backend handles the data storage (SQLite) and provides the API for the study plan and progress tracking.

1. **Navigate to the backend directory:**
   ```powershell
   cd Internal_Study_plan_App/backend
   ```

2. **Set up a Virtual Environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies:**
   Since no `requirements.txt` is present, install the core requirements:
   ```powershell
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

4. **Initialize/Seed the Database:**
   Run the seed script to populate the roadmap data:
   ```powershell
   python seed_db.py
   ```

5. **Start the Backend Server:**
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```
   The backend will be available at `http://localhost:8000`.

---

## 💻 Frontend Setup (React + Vite)

The frontend provides a modern, glassmorphism-styled interface to visualize the roadmap and track daily tasks.

1. **Navigate to the frontend directory:**
   ```powershell
   cd Internal_Study_plan_App/frontend
   ```

2. **Install Dependencies:**
   ```powershell
   npm install
   ```

3. **Start the Development Server:**
   ```powershell
   npm run dev
   ```
   The application will usually be available at `http://localhost:5173` (or the port specified in your terminal).

---

## 📖 How to Use
- **Track Progress**: Click on any task to toggle its completion status.
- **Visual Feedback**: The progress bar and stats cards at the top will update in real-time as you complete tasks.
- **Phase Breakdown**: Use the accordion-style phase headers to expand or collapse specific sections of the roadmap.

## 🏗️ Project Structure
- `backend/`: FastAPI application, database models, and seeding scripts.
- `frontend/`: React application with Vite, styled with custom CSS for a premium feel.
- `study_plan.db`: SQLite database storing your personal progress.
