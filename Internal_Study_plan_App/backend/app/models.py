from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Phase(Base):
    __tablename__ = "phases"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    start_day = Column(Integer)
    end_day = Column(Integer)
    days = relationship("Day", back_populates="phase")

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    phase_id = Column(Integer, ForeignKey("phases.id"))
    day_number = Column(Integer)
    phase = relationship("Phase", back_populates="days")
    tasks = relationship("Task", back_populates="day")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("days.id"))
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    day = relationship("Day", back_populates="tasks")
