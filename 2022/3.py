import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)


def getValue(x):
  if 97 <= ord(x) <= 122:
    return ord(x) - 96
  elif 65 <= ord(x) <= 90:
    return ord(x) - 38


f = open("3.in", "r")
lines = f.read().splitlines()
ans = []

if sys.argv[1] == "1":
  # part 1
  for l in lines:
    c1 = sorted([x for x in l[:int(len(l) / 2)]])
    c2 = sorted([y for y in l[int(len(l) / 2):]])
    for i, v in enumerate(c1):
      if v in c2:
        break
    ans.append(v)

elif sys.argv[1] == "2":
  # part 2
  for r in range(0, len(lines), 3):
    c1 = [x for x in lines[r + 0]]
    c2 = [x for x in lines[r + 1]]
    c3 = [x for x in lines[r + 2]]
    for i, v in enumerate(c1):
      if v in c2 and v in c3:
        break
    ans.append(v)

s = 0
for x in ans:
  s += getValue(x)
print(s)

f.close()
