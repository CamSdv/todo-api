from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []
current_id = 1


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: dict):
    global current_id

    new_task = {
        "id": current_id,
        "title": task["title"],
        "completed": False
    }

    tasks.append(new_task)
    current_id += 1

    return new_task


@app.put("/tasks/{id}")
def update_task(id: int, task: dict):

    for t in tasks:
        if t["id"] == id:
            t["title"] = task["title"]
            t["completed"] = task["completed"]
            return t

    raise HTTPException(status_code=404,
                        detail="Task not found")


@app.delete("/tasks/{id}")
def delete_task(id: int):

    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return {
                "message": "Task deleted"
            }

    raise HTTPException(status_code=404, detail="Task not found")