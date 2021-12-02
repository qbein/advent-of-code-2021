def part0201():
  """
  Advent of Code 2021; December 2nd, part 1
  """
  horizontal = 0
  vertical = 0

  file = open("data_02.txt", "r")
  for line in file:
    # forward 7
    parts = line.split()
    if(parts[0] == "forward"):
      horizontal += int(parts[1])
    if(parts[0] == "down"):
      vertical += int(parts[1])
    if(parts[0] == "up"):
      vertical -= int(parts[1])

  print("December 2, Part 1; result: {0}".format(horizontal * vertical))

def part0202():
  """
  Advent of Code 2021; December 2nd, part 2
  """
  horizontal = 0
  vertical = 0
  aim = 0

  file = open("data_02.txt", "r")
  for line in file:
    # forward 7
    parts = line.split()
    if(parts[0] == "forward"):
      move = int(parts[1])
      horizontal += move
      vertical += move * aim
    if(parts[0] == "down"):
      aim += int(parts[1])
    if(parts[0] == "up"):
      aim -= int(parts[1])

  print("December 2, Part 2; result: {0}".format(horizontal * vertical))