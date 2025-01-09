from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base



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
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(Integer, default=0)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    user = relationship("Task", back_populates='user')
