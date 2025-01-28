from fastapi import APIRouter
from pydantic import BaseModel

router_t = APIRouter(prefix="/task", tags=["task"])

@router_t.get("/")
async def all_tasks():
    pass

@router_t.get("/task_id")
async def task_by_id():
    pass

@router_t.post("/create")
async def create_task():
    pass

@router_t.put("/update")
async def update_task():
    pass

@router_t.delete("/delete")
async def delete_task():
    pass
