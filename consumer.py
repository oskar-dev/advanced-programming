import util
import time

class Task:
    def __init__(self, id: int, status: str, duration: int):
        self.id = id
        self.status = status
        self.duration = duration

def get_task() -> Task:
    util.cur.execute("SELECT * FROM tasks WHERE status = 'pending' LIMIT 1")
    row = util.cur.fetchone()
    if row:
        return Task(row[0], row[1], row[2])
    else:
        return None

def update_task(task: Task) -> None:
    util.cur.execute("UPDATE tasks SET status = ? WHERE id = ?", (task.status, task.id))
    util.con.commit()

while True:
    task = get_task()

    if not task:
        print("No pending tasks found.")
        time.sleep(5)
        continue

    task.status = "in_progress"

    update_task(task)

    print(f"Processing task {task.id} for {task.duration} seconds...")
    time.sleep(task.duration)

    task.status = "completed"
    update_task(task)

    time.sleep(5)
        