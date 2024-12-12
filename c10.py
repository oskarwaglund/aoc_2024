import common

data = common.ReadInputAsIntMap(10)
h = len(data)
w = len(data[0])

trailheads = set()
for y in range(h):
  for x in range(w):
    if data[y][x] == 0:
      trailheads.add((x, y))

uniquePaths = 0

def search(x, y, data):
  level = data[y][x]
  if level == 9:
    global uniquePaths
    uniquePaths += 1
    return set([(x, y)])

  summits = set()
  dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
  for d in dir:
    nx = x+d[0]
    ny = y+d[1]
    if not common.Inside(nx, ny, len(data[0]), len(data)):
      continue

    if data[ny][nx] == level+1:
      summits.update(search(nx, ny, data))

  return summits

p1 = 0
for t in trailheads:
  summits = search(t[0], t[1], data)
  p1 += len(summits)

print(p1)
print(uniquePaths)