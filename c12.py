import common

def flood(type, x, y, data, area):
  global w, h
  if not common.Inside(x, y, w, h):
    return area

  if (x, y) not in area and data[y][x] == type:
    area.add((x, y))
  else:
    return area

  dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
  for d in dirs:
    area = flood(type, x+d[0], y+d[1], data, area)
  return area

def circumference(area):
  global w, h
  c = 0
  for (x, y) in area:
    dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
    for d in dirs:
      (dx, dy) = (x+d[0], y+d[1])
      if not common.Inside(dx, dy, w, h) or (dx, dy) not in area:
        c += 1
  return c

#Return number of sides of an area
def findSides(area):
  seg=[]

  for (x, y) in area:
    dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
    for d in dirs:
      (dx, dy) = (x+d[0], y+d[1])
      if not common.Inside(dx, dy, w, h) or (dx, dy) not in area:
        seg.append((x, y, d))

  sides = 0
  while len(seg) > 0:
    start = seg.pop()
    direc = (1, 0) if start[2][0] == 0 else (0, 1)
    probe = (start[0]+direc[0], start[1]+direc[1], start[2])
    while probe in seg:
      seg.remove(probe)
      probe = (probe[0]+direc[0], probe[1]+direc[1], probe[2])
    probe = (start[0]-direc[0], start[1]-direc[1], start[2])
    while probe in seg:
      seg.remove(probe)
      probe = (probe[0]-direc[0], probe[1]-direc[1], probe[2])
    sides += 1

  return sides

data = common.ReadInput(12)
#data = common.ReadInputFn("i12_1.txt")
w = len(data[0])
h = len(data)

areas = []

for x in range(w):
  for y in range(h):
    if any([(x,y) in a for a in areas]):
      continue
    area = flood(data[y][x], x, y, data, set())
    areas.append(area)

p1 = 0
for a in areas:
  p1 += len(a) * circumference(a)
print(p1)

p2 = 0
for a in areas:
  p2 += len(a) * findSides(a)
print(p2)