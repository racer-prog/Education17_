from fastapi import APIRouter
from pydantic import BaseModel

router_u = APIRouter(prefix="/user", tags=["user"])

@router_u.get("/")
async def all_users():
    pass

@router_u.get("/user_id")
async def user_by_id():
    pass

@router_u.get("/create")
async def create_user():
    pass

@router_u.post("/update")
async def update_user():
    pass

@router_u.delete("/delete")
async def delete_user():
    pass