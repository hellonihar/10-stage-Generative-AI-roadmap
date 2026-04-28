from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="90-Day GenAI Study Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic Schemas
class TaskBase(BaseModel):
    id: int
    description: str
    is_completed: bool

    class Config:
        from_attributes = True


class DayBase(BaseModel):
    id: int
    day_number: int
    tasks: List[TaskBase]

    class Config:
        from_attributes = True


class PhaseBase(BaseModel):
    id: int
    title: str
    description: str
    start_day: int
    end_day: int
    days: List[DayBase]

    class Config:
        from_attributes = True


@app.get("/plan", response_model=List[PhaseBase])
def get_plan(db: Session = Depends(database.get_db)):
    phases = db.query(models.Phase).all()
    return phases


@app.get("/stats")
def get_stats(db: Session = Depends(database.get_db)):
    total_tasks = db.query(models.Task).count()
    completed_tasks = (
        db.query(models.Task).filter(models.Task.is_completed == True).count()
    )
    return {
        "total": total_tasks,
        "completed": completed_tasks,
        "percent": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
    }


@app.patch("/tasks/{task_id}")
def toggle_task(
    task_id: int, is_completed: bool, db: Session = Depends(database.get_db)
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.is_completed = is_completed
    db.commit()
    db.refresh(task)
    return {"status": "success", "task_id": task_id, "is_completed": task.is_completed}
