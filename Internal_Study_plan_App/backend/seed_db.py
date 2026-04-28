from app.database import SessionLocal, engine
from app import models

def seed():
    db = SessionLocal()
    models.Base.metadata.create_all(bind=engine)

    # Check if data already exists
    if db.query(models.Phase).first():
        print("Database already seeded.")
        return

    phases_data = [
        {"title": "Phase 1: Foundations", "start": 1, "end": 20, "desc": "Python, Data, ML basics"},
        {"title": "Phase 2: Deep Learning + Transformers", "start": 21, "end": 40, "desc": "Neural networks and transformers"},
        {"title": "Phase 3: LLMs + Embeddings", "start": 41, "end": 60, "desc": "Prompting and vector databases"},
        {"title": "Phase 4: RAG Systems", "start": 61, "end": 75, "desc": "Retrieval-augmented generation"},
        {"title": "Phase 5: Applications + Deployment", "start": 76, "end": 85, "desc": "Agents and deployment"},
        {"title": "Phase 6: Advanced", "start": 86, "end": 90, "desc": "Fine-tuning, guardrails, evaluation"}
    ]

    # Specific tasks for early days (based on OCR)
    daily_tasks = {
        1: ["Setup Python, VS Code, virtualenv", "Revise basics: variables, loops"],
        2: ["Work with APIs using requests", "Parse JSON responses"],
        3: ["NumPy arrays and operations"],
        4: ["Pandas basics: load and filter data"],
        5: ["Data cleaning and preprocessing"],
        6: ["Build data processing script"],
        7: ["Expose dataset via FastAPI"],
        8: ["Modular coding practices"],
        9: ["FastAPI deeper concepts"],
        10: ["Connect API with dataset"],
        11: ["Add search/filter endpoints"],
        12: ["Logging and error handling"],
        13: ["Finalize API project"],
        14: ["Push to GitHub"],
        15: ["ML basics overview"],
        16: ["Regression models"],
        17: ["Classification models"],
        18: ["Evaluation metrics"],
        19: ["Overfitting concepts"],
        20: ["Build ML API"]
    }

    for p in phases_data:
        phase = models.Phase(title=p["title"], description=p["desc"], start_day=p["start"], end_day=p["end"])
        db.add(phase)
        db.flush()

        for day_num in range(p["start"], p["end"] + 1):
            day = models.Day(phase_id=phase.id, day_number=day_num)
            db.add(day)
            db.flush()

            tasks = daily_tasks.get(day_num, [f"Focus on core topic for day {day_num}", "Implement mini task/project"])
            for task_desc in tasks:
                task = models.Task(day_id=day.id, description=task_desc)
                db.add(task)
    
    db.commit()
    print("Seeding completed successfully!")

if __name__ == "__main__":
    seed()
