import common
import copy

#return true if in a loop
def isInfinite(mmap, x, y, dirIndex):
  #Track position and direction
  visited = set()

  dirs = [[0,-1],[1,0],[0,1],[-1,0]]
  while(True):
    if((x,y,dirIndex) in visited):
      return True
    visited.add((x,y,dirIndex))
    dir = dirs[dirIndex]
    nextX, nextY = x + dir[0], y + dir[1]
    if(not (nextX >= 0 and nextX < W and nextY >= 0 and nextY < H)):
      return False
    if(mmap[nextY][nextX] == "#"):
      dirIndex = (dirIndex+1)%4
    else:
      x, y = nextX, nextY

mmap = common.ReadInput(6)
#Convert str to list
for i in range(len(mmap)):
  mmap[i] = list(mmap[i])
sy = 0
sx = -1
for l in mmap:
  for X in range(len(l)):
    if l[X] == "^":
      sx = X
      break
  if(sx >= 0):
    break
  sy += 1

W = len(mmap[0])
H = len(mmap)

visited = set()

x, y = sx, sy

dirs = [[0,-1],[1,0],[0,1],[-1,0]]
dirIndex = 0
p2Start = dict()
while(x >= 0 and x < W and y >= 0 and y < H):
  visited.add((x,y))
  dir = dirs[dirIndex]
  nextX, nextY = x + dir[0], y + dir[1]
  if(not (nextX >= 0 and nextX < W and nextY >= 0 and nextY < H)):
    break
  if(mmap[nextY][nextX] == "#"):
    dirIndex = (dirIndex+1)%4
  else:
    x, y = nextX, nextY
    if not (x,y) in p2Start:
      p2Start[(x, y)] = (x-dirs[dirIndex][0], y-dirs[dirIndex][1], dirIndex)

print(len(visited))

p2 = 0

for (xx, yy) in visited:
  if(mmap[yy][xx] in "^#"):
    continue
  mmap[yy][xx] = "#"
  (sx, sy, dirIndex) = p2Start[(xx, yy)]
  if(isInfinite(mmap, sx, sy, dirIndex)):
    p2 += 1
  mmap[yy][xx] = "."

print(p2)