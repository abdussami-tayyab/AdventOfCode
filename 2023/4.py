from collections import defaultdict
import sys

P1 = 0
P2 = defaultdict(int)

with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]

  # store originals
  for idx, line in enumerate(lines):
    P2[idx + 1] += 1

  for idx, line in enumerate(lines):
    group = line.split(": ")[1]
    group = group.strip()
    winning = group.split(" | ")[0]
    haves = group.split(" | ")[1]

    winning = sorted([int(x) for x in winning.split()])
    haves = sorted([int(x) for x in haves.split()])

    count = 0
    for have in haves:
      if have in winning:
        count += 1

    # generate copies of next cards for part 2
    curr = idx + 1
    for i in range(P2[curr]):
      next = curr + 1
      for j in range(count):
        P2[next] += 1
        next += 1

    if count != 0:
      P1 += 2 ** (count - 1)

P2sum = 0
for k, v in P2.items():
  P2sum += v

print(f"Part 1: {P1}")
print(f"Part 2: {P2sum}")
