from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FASTAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

app.add_middleware(
    CORSMiddleware,,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"])

class Task(BaseModel):
    title=str
tasks: List[Task] = []
@app.post("/tasks/")
def create_task(task:Task)
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}
@app.get("/tasks/")
def get_tasks():
    return tasks