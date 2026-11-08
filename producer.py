import os


def get_task_id() -> int:
    id = 0

    if not os.path.isfile("memory"):
        with open("memory", "x") as f:
            f.write("id=1")
        return 0

    with open("memory", "r") as f:
        line = f.readline().split("=")


def spawn_task():

    with open("queue.csv", "a") as f:
        f.write("")
