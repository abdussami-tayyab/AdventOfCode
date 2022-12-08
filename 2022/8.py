from math import prod
import sys


def checkView(S, x, y, v, mode):
  score = 0
  if mode == "l":
    for l in range(y, -1, -1):
      score += 1
      if S[x][l] >= v:
        return score, False
  elif mode == "t":
    for l in range(x, -1, -1):
      score += 1
      if S[l][y] >= v:
        return score, False
  elif mode == "r":
    for l in range(y, LIMIT, 1):
      score += 1
      if S[x][l] >= v:
        return score, False
  elif mode == "b":
    for l in range(x, LIMIT, 1):
      score += 1
      if S[l][y] >= v:
        return score, False

  return score, True


if __name__ == '__main__':
  f = open("8.in", "r")
  lines = f.read().splitlines()

  S = []
  LIMIT = len(lines)
  bounds = LIMIT + (LIMIT - 2) * 2

  if len(sys.argv) == 1:
    print("ERROR: Enter part # as argument")
    sys.exit(0)

  # which part
  p1, p2 = False, False

  if sys.argv[1] == "1":
      p1 = True
  else:
      p2 = True


  for line in lines:
    t = []
    for x in line:
      t.append(int(x))
    S.append(t)

  A = []
  for x in range(1, LIMIT - 1):
    for y in range(1, LIMIT - 1):
      v = S[x][y]
      visible = [True, True, True, True]
      scores = [0, 0, 0, 0]
      scores[0], visible[0] = checkView(S, x, y - 1, v, "l")
      scores[1], visible[1] = checkView(S, x - 1, y, v, "t")
      scores[2], visible[2] = checkView(S, x, y + 1, v, "r")
      scores[3], visible[3] = checkView(S, x + 1, y, v, "b")

      if p1:
        if any([x for x in visible]):
          A.append((x, y))
      else:
        A.append(prod(scores))

  if p1:
    print(((LIMIT * 4) - 4) + len(A))
  else:
    print(max(A))
