
def ReadInputFn(filename):
  lines = []
  with open(filename, 'r') as f:
    for line in f:
      lines.append(line.strip())
  return lines

def ReadInput(day):
  return ReadInputFn(f'i{day}.txt')

def ReadInputAsIntMap(day):
  lines = []
  with open(f'i{day}.txt', 'r') as f:
    for line in f:
      lines.append([int(a) for a in line.strip()])
  return lines

def Inside2(x, y, xMin, xMax, yMin, yMax):
  return xMin <= x <= xMax and yMin <= y <= yMax

def Inside(x, y, w, h):
  return Inside2(x, y, 0, w-1, 0, h-1)