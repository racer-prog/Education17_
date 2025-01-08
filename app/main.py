from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug = True)

from routers.task import router_task as task_router
from routers.user import router_user as user_router

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

