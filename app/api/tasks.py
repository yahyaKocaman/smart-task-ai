from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.domain.models import Task
from app.infrastructure.ai_service import AIService

router = APIRouter()
ai = AIService()

@router.post("/")
def create_task(title: str, description: str, db: Session = Depends(get_db)):
    priority = ai.predict_priority(description)
    task = Task(title=title, description=description, priority=priority)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()