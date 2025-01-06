from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

router = APIRouter(prefix="/task", tags="[task]")


@router.get("/", response_class=HTMLResponse)
async def all_tasks(request: Request):
    pass


@router.get("/task_id", response_class=HTMLResponse)
async def task_by_id(request: Request):
    pass


@router.post("/create", response_class=HTMLResponse)
async def create_task(request: Request):
    pass


@router.put("/update", response_class=HTMLResponse)
async def update_task(request: Request):
    pass


@router.delete("/delete", response_class=HTMLResponse)
async def delete_task(request: Request):
    pass