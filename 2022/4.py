import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)

f = open("4.in", "r")
lines = f.read().splitlines()

if sys.argv[1] == "1":
  # part 1
  count = 0
  for line in lines:
    p1, p2 = line.split(",")
    s1, e1 = p1.split("-")
    s2, e2 = p2.split("-")
    if (int(s2) >= int(s1) and int(e2) <= int(e1)) or (int(s1) >= int(s2) and int(e1) <= int(e2)):
      count += 1
  print(count)

elif sys.argv[1] == "2":
  # part 2
  fail = 0
  for line in lines:
    p1, p2 = line.split(",")
    s1, e1 = p1.split("-")
    s2, e2 = p2.split("-")
    if int(s2) > int(e1) or int(e2) < int(s1):
      fail += 1
  print(len(lines) - fail)

f.close()
