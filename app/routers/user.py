from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

router = APIRouter(prefix="/user", tags="[user]")


@router.get("/", response_class=HTMLResponse)
async def all_users(request: Request):
    pass


@router.get("/user_id", response_class=HTMLResponse)
async def user_by_id(request: Request):
    pass


@router.post("/create", response_class=HTMLResponse)
async def create_user(request: Request):
    pass


@router.put("/update", response_class=HTMLResponse)
async def update_user(request: Request):
    pass


@router.delete("/delete", response_class=HTMLResponse)
async def delete_user(request: Request):
    pass