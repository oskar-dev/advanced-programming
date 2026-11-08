import os

import argparse

def get_task_id() -> int:
    id = 0

    if not os.path.isfile("memory"):
        with open("memory", "x") as f:
            f.write("id=1")
        return 0
    with open("memory", "r") as f:
        line = f.readline().split("=")

        id = int(line[1])
    with open("memory", "w") as f:
        f.write(f"id={id + 1}")
    return id

def spawn_task(id: int) -> None:

    task = f"{id};pending;30"

    with open("queue.csv", "a") as f:
        f.write(task + "\n")

parser = argparse.ArgumentParser("Task Producer")
parser.add_argument("--count", type=int, default=1, help="Number of tasks to spawn")

args = parser.parse_args()

for _ in range(args.count):
    taks_id = get_task_id()

    spawn_task(taks_id)

    print(f"Task({taks_id}) spawned successfully.")