import time

class Task:
    def __init__(self, id: int, status: str, duration: int) -> None:
        self.id = id
        self.status = status
        self.duration = duration

def consume_task() -> Task:

    lines = []
    with open("queue.csv", "r") as f:
        lines = f.readlines()

    if not lines:
        print("No tasks in the queue.")
        return

    for i, line in enumerate(lines):
        task_data = line.strip().split(";")
        if task_data[1] == "pending":
            task = Task(int(task_data[0]), task_data[1], int(task_data[2]))
            lines[i] = f"{task.id};in_progress;{task.duration}\n"
            break

    with open("queue.csv", "w") as f:
        f.writelines(lines)

    return task

def do_task(task: Task) -> None:
    print(f"Doing Task({task.id}) for {task.duration} seconds...")
    
    time.sleep(task.duration)

    lines = []
    with open("queue.csv", "r") as f:
        lines = f.readlines()

    if not lines:
        print("No tasks in the queue.")
        return

    for i, line in enumerate(lines):
        tmp_data = line.strip().split(";")
        if int(tmp_data[0]) == task.id:
            lines[i] = f"{task.id};done;{task.duration}\n"
            break

    with open("queue.csv", "w") as f:
        f.writelines(lines)

    print(f"Task({task.id}) completed.")

while True:
    task = consume_task()

    do_task(task)

    time.sleep(5)