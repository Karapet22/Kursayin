import asyncio

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Write async code", "completed": True},
]

async def get_all_tasks():
    await asyncio.sleep(1)  
    return tasks

async def get_task_by_id(task_id: int):
    await asyncio.sleep(1)
    return next((t for t in tasks if t["id"] == task_id), None)

async def create_task(task):
    await asyncio.sleep(1)
    tasks.append(task)
    return task
