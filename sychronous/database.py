import time

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Write sync code", "completed": True},
]

def get_all_tasks():
    time.sleep(1)   
    return tasks

def get_task_by_id(task_id: int):
    time.sleep(1)
    return next((t for t in tasks if t["id"] == task_id), None)

def create_task(task):
    time.sleep(1)
    tasks.append(task)
    return task
