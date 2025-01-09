from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from user import import *



router_task = APIRouter(prefix="/task", tags=["task"])


@router_task.get("/")
async def all_tasks():
    pass


@router_task.get("/task_id")
async def task_by_id():
    pass


@router_task.post("/create")
async def create_task():
    pass


@router_task.put("/update")
async def update_task():
    pass


@router_task.delete("/delete")
async def delete_task():
    pass

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates='tasks')

