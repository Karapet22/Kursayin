from fastapi import FastAPI, HTTPException
from models import Task
from database import get_all_tasks, get_task_by_id, create_task

app = FastAPI(title="Sync Task Manager")

@app.get("/tasks")
def list_tasks():
    return get_all_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks")
def add_task(task: Task):
    return create_task(task.dict())
