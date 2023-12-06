from collections import defaultdict
import re
import sys


values = defaultdict(int)
P1 = defaultdict(int)
P2 = 0
part = sys.argv[2]


with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]

  times = [int(x) for x in re.findall(r"\d+", lines[0])]
  distances = [int(x) for x in re.findall(r"\d+", lines[1])]

  # storing time:distance
  for i in range(len(times)):
    values[times[i]] = distances[i]

  for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    P1Seconds = []

    for second in range(1, time, 1):
      remaining = time - second
      total = remaining * second

      # as long as we are above distance threshold, keep going
      if total > distance:
        if part == "p2":
          P2 = time - (2 * second) + 1
          break
        else:
          P1[time] += 1
          P1Seconds.append(total)
      # the moment we see downwards trajectory, we stop
      elif len(P1Seconds) > 0 and total < max(P1Seconds):
        break

  # calculation for part 1
  total = 1
  for x in P1.values():
    total *= x

  if part == "p1":
    print(f"P1: {total}")
  else:
    print(f"P2: {P2}")
