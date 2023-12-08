from collections import defaultdict
from math import gcd
import sys

maps = defaultdict(list)
part = sys.argv[2]

with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]

  turns = [x for x in lines[0]]
  groups = lines[2:]
  for group in groups:
    source, dest = group.split("=")
    source = source.strip()
    left, right = dest.split(", ")
    left = left.replace("(", "").strip()
    right = right.replace(")", "").strip()

    maps[source] = [left, right]

  # getting start
  if part == "p1":
    start = None
    while True:
      start = [item for (item, value) in maps.items() if item == "AAA"][0]
      break
  else:
    starts = [item for (item, _) in maps.items() if item[2] == "A"]

  turnIdx = 0
  count = 0
  if part == "p2":
    firstFinds = [-1 for _ in starts]
  while (part == "p2" and -1 in firstFinds) or (part == "p1" and True):
    if part == "p2":
      for idx, start in enumerate(starts):
        turn = turns[turnIdx]

        starts[idx] = maps[start][0] if turn == "L" else maps[start][1]
        if starts[idx][2] == "Z" and firstFinds[idx] == -1:
          firstFinds[idx] = count + 1
    else:
      turn = turns[turnIdx]

      if start == "ZZZ":
        break

      start = maps[start][0] if turn == "L" else maps[start][1]

    turnIdx = 0 if turnIdx == len(turns) - 1 else turnIdx + 1
    count += 1

  if part == "p2":
    P2 = 1
    for find in firstFinds:
        P2 = P2 * find // gcd(P2, find)
    print(f"Part 2: {P2}")
  else:
    print(f"Part 1: {count}")
