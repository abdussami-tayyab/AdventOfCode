import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)


f = open(sys.argv[1], "r")
lines = [l.strip() for l in f.read().split("\n")]
lines = lines[:-1]
f.close()


# Part 1
A = []
for line in lines:
  num1 = -1
  num2 = -1
  for char in line:
    if char.isnumeric() and num1 == -1:
      num1 = int(char)
    elif char.isnumeric():
      num2 = int(char)
  if num2 == -1:
    num2 = num1
  num = num1*10 + num2*1
  A.append(num)

print(f"Part 1: {sum(A)}")


# Part 2
numbers = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
  'zero': '0'
}

def get_num(line, reverse=False):
  A = []

  # Find the smallest/largest index of a number
  for number in numbers:
    index = -1
    if reverse:
      index = line.rfind(number)
    else:
      index = line.find(number)
    if index != -1:
      A.append({
        "index": index,
        "number": number
      })

  A = sorted(A, key=lambda d: d["index"], reverse=reverse)

  # Replace word number with number
  if len(A) > 0:
    number = A[0]["number"]
    position = A[0]["index"]
    line = line[:position] + numbers[number] + line[position + len(number):]

  # Do the math
  num1 = -1
  line = line[::-1] if reverse else line
  for char in line:
    if char.isnumeric() and num1 == -1:
      num1 = int(char)
      if not reverse:
        return num1 * 10
      else:
        return num1

total = 0
for line in lines:
  origline = line

  first = get_num(line)
  second = get_num(line, reverse=True)
  total += (first + second)

print(f"Part 2: {total}")
