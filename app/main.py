from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug = True)

from routers.task import *
from routers.user import *

@app.get("/", response_class=HTMLResponse)
async def welcome(request: Request) -> dict:
    return {"message": "Welcome to Taskmanager"}
