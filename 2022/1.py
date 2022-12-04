import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)


f = open("1.in", "r")
lines = [l.strip() for l in f.read().split("\n\n")]

A = []
for nums in lines:
  nums = nums.split("\n")
  s = sum([int(x) for x in nums])
  A.append(s)

if sys.argv[1] == "1":
  print(max(A))
else:
  print(sum(sorted(A, reverse=True)[:3]))

f.close()
