# Implementation Plan: 90-Day Generative AI Study Plan Tracker

This document outlines the plan to build a web application for tracking the 90-day Generative AI study roadmap.

## 1. Project Architecture

### Backend (FastAPI + SQLite)
- **Framework**: FastAPI for high-performance async API.
- **Database**: SQLite for lightweight, file-based storage.
- **ORM**: SQLAlchemy or SQLModel for database interactions.
- **Schema**:
  - `Phases`: Groups days into logical sections (Foundations, LLMs, etc.).
  - `Days`: Individual days (1-90) linked to phases.
  - `Tasks`: Specific learning objectives for each day.

### Frontend (React + Premium CSS)
- **Framework**: React (Vite) for a responsive SPA.
- **Styling**: Vanilla CSS with a modern, premium aesthetic (Dark Mode, Glassmorphism).
- **Icons**: Lucide-React or similar for clean, minimal icons.
- **Charts**: Recharts or simple SVG-based progress visualizations.

## 2. Feature Roadmap

### Phase 1: Data Preparation & Backend Setup
- [ ] Parse PDF content into a structured JSON format.
- [ ] Initialize FastAPI project with SQLite connection.
- [ ] Implement database migration/seeding script to populate the 90-day plan.
- [ ] Create API endpoints:
  - `GET /plan`: Fetch the entire roadmap.
  - `PATCH /tasks/{id}`: Toggle task completion.
  - `GET /stats`: Get progress percentages and streak data.

### Phase 2: Frontend Foundation
- [ ] Initialize React app in `Internal_Study_plan_App/frontend`.
- [ ] Design the core Design System (colors, spacing, glassmorphism utilities).
- [ ] Build reusable components:
  - `ProgressBar`: Circular and linear progress indicators.
  - `DayCard`: Individual day summary with checkboxes.
  - `PhaseAccordion`: Grouping days by phase.

### Phase 3: Interactive Dashboard
- [ ] Implement the main dashboard view with high-level stats.
- [ ] Add the "Daily Focus" section highlighting the current day's tasks.
- [ ] Integrate animations (Framer Motion or CSS Transitions) for state changes.

### Phase 4: Polish & Refinement
- [ ] Add persistence (local storage or backend sync).
- [ ] Ensure mobile responsiveness.
- [ ] Final UI/UX audit for "Premium" feel.

## 3. Data Schema (Draft)

```sql
CREATE TABLE phases (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    start_day INTEGER,
    end_day INTEGER
);

CREATE TABLE days (
    id INTEGER PRIMARY KEY,
    phase_id INTEGER,
    day_number INTEGER,
    FOREIGN KEY(phase_id) REFERENCES phases(id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    day_id INTEGER,
    description TEXT NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY(day_id) REFERENCES days(id)
);
```

## 4. Design Aesthetics
- **Background**: Deep midnight blue gradient (`#0f172a` to `#1e293b`).
- **Cards**: Translucent glassmorphism (`backdrop-filter: blur(10px)`).
- **Accents**: Cyber-cyan (`#22d3ee`) and Neon-purple (`#818cf8`) for progress bars.
- **Typography**: Inter or Outfit (Google Fonts) for a modern tech feel.
