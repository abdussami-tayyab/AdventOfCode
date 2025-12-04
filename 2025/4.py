import sys


def run(grid):
    # To keep track of met coords
    met = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            roll = grid[i][j]
            # Skip empty spots
            if roll == '.':
                continue

            forklifts = 0
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if x == 0 and y == 0:
                        continue

                    dx = i + x
                    dy = j + y
                    if (0 <= dx < len(grid)) and (0 <= dy < len(grid)):
                        forklifts += 1 if grid[dx][dy] == '@' else 0

            # Given constraint
            if forklifts < 4:
                met.append((i, j))

    return met


if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], "r") as f:
        grid = f.read().split("\n")

    p1 = sys.argv[2] == "p1"

    while True:
        met = run(grid)
        if p1:
            print(len(met))
            break

        # Mark met coords
        for (x, y) in met:
            l = list(grid[x])
            l[y] = 'x'
            grid[x] = ''.join(l)

        # Keep printing value until we see repeat as loop is endless, then break, in case of p2
        print(len(met))
