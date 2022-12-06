import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)

# which part
p1, p2 = False, False

if sys.argv[1] == "1":
    p1 = True
else:
    p2 = True

s = "loremipsumdolormit"

if p1:
  for i in range(len(s) - 3):
    x = set(s[i:i + 4])
    if len(x) == 4:
      print(i + 4)
      sys.exit(0)

if p2:
  for i in range(len(s) - 13):
    x = set(s[i:i + 14])
    if len(x) == 14:
      print(i + 14)
      sys.exit(0)
