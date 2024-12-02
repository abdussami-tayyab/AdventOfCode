# Please don't try to hire me from this piece of code, having a bad day.

from copy import deepcopy
import sys


if len(sys.argv) == 1:
  print("ERROR: Enter file name (2.in, 2.ex) as arg")
  sys.exit(0)


def checkList(L, again=False):
    idx = 1
    order = 1 if L[0] > L[1] else 0

    for curr in L[1:]:
        prev = L[idx - 1]
        order_check = True
        if order == 1 and curr >= prev:
            order_check = False
        if order == 0 and curr <= prev:
            order_check = False
        if not order_check or not abs(curr - prev) in (1, 2, 3):
            return False
        idx += 1

    return True


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
        total = len(lines)

        unsafe = []
        for line in lines:
            L = [int(x) for x in line.strip().split(" ")]
            if not checkList(L):
                unsafe.append(L)

        print(f"p1: {total - len(unsafe)}")

        p2 = 0
        for L in unsafe:
            a = 0
            for i in range(len(L)):
                temp = deepcopy(L)
                del temp[a]
                if checkList(temp):
                    p2 += 1
                    break
                a += 1

        print(f"p2: {total - len(unsafe) + p2}")
