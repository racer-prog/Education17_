from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from task import import *


router_user = APIRouter(prefix="/user", tags=["user"])


@router_user.get("/")
async def all_users():
    pass


@router_user.get("/user_id")
async def user_by_id():
    pass


@router_user.post("/create")
async def create_user():
    pass


@router_user.put("/update")
async def update_user():
    pass


@router_user.delete("/delete")
async def delete_user():
    pass

class User(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates='tasks')