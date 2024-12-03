import re


def execute_instructions(pattern, string):
    # find all mul(X,Y) instructions from string
    instructions = re.findall(pattern, string)
    total = 0

    for instruction in instructions:
        # get values from instruction e.g. mul(X,Y)
        values = instruction[4:-1]
        a, b = map(int, values.split(","))

        total += (a * b)

    return total


if __name__ == '__main__':
    pattern = "mul\(\d+,\d+\)"
    string = """input_string"""

    # for Part 1, we only need to fetch `mul(X,Y)` instructions
    print(f"p1: {execute_instructions(pattern, string)}")

    # for Part 2, we need mul(X,Y) instructions that come after a do() and before a don't() instruction
    dos = string.split("do()")
    p2 = 0
    for do in dos:
        do = do.split("don't()")[0]

        p2 += execute_instructions(pattern, do)

    print(f"p2: {p2}")
