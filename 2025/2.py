import sys

def runP1(x, y):
    total = 0

    for i in range(x, y + 1):
        repr = str(i)
        # Skip odd numbers
        if len(repr) % 2 != 0:
            continue

        # Get length of number and halve it
        number = str(repr)
        length = len(str(number))
        left = 0
        right = length // 2
        valid = True

        # Keep running until left and right halves are the same
        while right < length:
            if int(number[left]) == int(number[right]):
                left += 1
                right += 1
            else:
                valid = False
                break

        if valid:
            total += i

    return total


def runP2(x, y):
    total = 0

    # Iterate through all numbers in range
    for i in range(x, y + 1):
        number = str(i)
        index = 0
        length = 1

        # Check repeating patterns, brute force but, meh
        while index < len(number):
            # Form the substring
            sofar = number[:length]
            # Count occurences of substring
            occurences = number.count(sofar)
            # Check if the substring repeated forms the entire number
            if length * occurences == len(number) and occurences > 1:
                total += i
                break
            index += 1
            length += 1

    return total


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.read().split("\n")[0]

    p1 = 0
    p2 = 0

    pairs = lines.split(",")
    for pair in pairs:
        x, y = map(int, pair.split("-"))
        p1 += runP1(x, y)
        p2 += runP2(x, y)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
