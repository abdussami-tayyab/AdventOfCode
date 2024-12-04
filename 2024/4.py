import sys


if len(sys.argv) == 1:
  print("ERROR: Enter file name (2.in, 2.ex) as arg")
  sys.exit(0)


def p1(word, max_row, max_col):
    count = 0

    for rdx, row in enumerate(word):
        for cdx, cell in enumerate(row):
            if cell == "X":
                # check if XMAS on the east
                if cdx < (max_col - 3) and (word[rdx][cdx + 1] == "M" and word[rdx][cdx + 2] == "A" and word[rdx][cdx + 3] == "S"):
                    count += 1
                # check if XMAS on the west
                if cdx > 2 and (word[rdx][cdx - 1] == "M" and word[rdx][cdx - 2] == "A" and word[rdx][cdx - 3] == "S"):
                    count += 1
                # check if XMAS to the north
                if rdx > 2 and (word[rdx - 1][cdx] == "M" and word[rdx - 2][cdx] == "A" and word[rdx - 3][cdx] == "S"):
                    count += 1
                # check if XMAS to the south
                if rdx < (max_row - 3) and (word[rdx + 1][cdx] == "M" and word[rdx + 2][cdx] == "A" and word[rdx + 3][cdx] == "S"):
                    count += 1
                # check if XMAS to north-east
                if (rdx > 2 and cdx < (max_col - 3)) and (word[rdx - 1][cdx + 1] == "M" and word[rdx - 2][cdx + 2] == "A" and word[rdx - 3][cdx + 3] == "S"):
                    count += 1
                # check if XMAS to north-west
                if (rdx > 2 and cdx > 2) and (word[rdx - 1][cdx - 1] == "M" and word[rdx - 2][cdx - 2] == "A" and word[rdx - 3][cdx - 3] == "S"):
                    count += 1
                # check if XMAS to south-west
                if (rdx < (max_row - 3) and cdx > 2) and (word[rdx + 1][cdx - 1] == "M" and word[rdx + 2][cdx - 2] == "A" and word[rdx + 3][cdx - 3] == "S"):
                    count += 1
                # check if XMAS to south-east
                if (rdx < (max_row - 3) and cdx < (max_col - 3)) and (word[rdx + 1][cdx + 1] == "M" and word[rdx + 2][cdx + 2] == "A" and word[rdx + 3][cdx + 3] == "S"):
                    count += 1

    return count

def p2(word, max_row, max_col):
    count = 0

    for rdx, row in enumerate(word):
        for cdx, cell in enumerate(row):
            if cell == "A" and (0 < rdx < max_row - 1) and (0 < cdx < max_col - 1):
                wordone = (word[rdx-1][cdx-1] + "A" + word[rdx+1][cdx+1])
                wordtwo = (word[rdx+1][cdx-1] + "A" + word[rdx-1][cdx+1])

                if ''.join(sorted(wordone)) == "AMS" and ''.join(sorted(wordtwo)) == "AMS":
                    count += 1

    return count


if __name__ == '__main__':
    word = []
    with open(sys.argv[1], "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            row = []
            for char in line:
                row.append(char)
            word.append(row)

    max_row = len(word)
    max_col = len(word[0])

    print(f"p1: {p1(word, max_row, max_col)}")
    print(f"p2: {p2(word, max_row, max_col)}")
