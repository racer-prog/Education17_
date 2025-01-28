from fastapi import FastAPI
from routers import task, user




app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to TaskManager"}

app.include_router(task.router_t)
app.include_router(user.router_u)