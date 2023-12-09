from collections import defaultdict
import sys

maps = defaultdict(list)
part = sys.argv[2]

with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]

  total = 0
  for line in lines:
    nums = [int(x) for x in line.split(" ")]
    history = [nums]

    while True:
      # do the math
      nums = [nums[idx + 1] - nums[idx] for idx in range(len(nums) - 1)]
      history.append(nums)

      # stop only if all items are 0
      if all([x == 0 for x in nums]):
        # pad an extra 0 to go back up
        history[-1].append(0)
        if part == "p2":
          history = [list(reversed(l)) for l in history]

        # add/subtract last items of lists
        for i in range(len(history) - 1, 0, -1):
          value = history[i - 1][-1] - history[i][-1] if part == "p2" else history[i - 1][-1] + history[i][-1]
          history[i - 1].append(value)

        # sum all next projected values of history
        total += history[0][-1]
        break

  print(total)
