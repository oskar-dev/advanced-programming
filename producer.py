import argparse

import util

parser = argparse.ArgumentParser("Task Producer")
parser.add_argument("--count", type=int, default=1, help="Number of tasks to spawn")

args = parser.parse_args()

for i in range(args.count):
    util.cur.execute("INSERT INTO tasks (status, duration) VALUES (?, ?)", ("pending", 30))
    util.con.commit()
    print("Task created")