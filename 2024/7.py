from collections import defaultdict
from itertools import product
import sys

p1 = True if sys.argv[2] == "p1" else False

def generate_operator_combinations(n):
    if n < 2:
        return []

    operators = ['+', '*', '|'] if not p1 else ['+', '*']
    return [''.join(combination) for combination in product(operators, repeat=n-1)]


with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")
    final = 0

    for idx, line in enumerate(lines):
        dest = int(line.split(":")[0])
        operands = list(map(int, line.split(": ")[1].split(" ")))

        combinations = generate_operator_combinations(len(operands))

        for combination in combinations:
            y = 1
            x = operands[0]

            for operator in list(combination):
                if operator == "+":
                    x += operands[y]
                elif operator == '*':
                    x *= operands[y]
                elif operator == '|':
                    x = int(f"{x}{operands[y]}")
                y += 1

            if x == dest:
                final += x  # found, break
                break

    print(final)
