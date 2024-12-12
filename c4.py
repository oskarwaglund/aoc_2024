import common

def countXmas(mMap, x, y, W, H):
  word = "XMAS"
  count = 0
  if(mMap[y][x] != word[0]):
    return 0
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if (dx == dy == 0):
        continue
      X = x
      Y = y
      score = 1
      for step in range(1, 4):
        X += dx
        Y += dy
        if(X < 0 or X >= W or Y < 0 or Y >= H):
          break
        if(mMap[Y][X] == word[step]):
          score += 1
        else:
          break
      if (score == 4):
        count += 1
  return count

def countX(mMap, x, y, W, H):
  if (x < 1 or x >= W-1 or y < 1 or y >= H-1):
    return 0
  if(mMap[y][x] != "A"):
    return 0
  word1 = mMap[y-1][x-1]+mMap[y][x]+mMap[y+1][x+1]
  word2 = mMap[y+1][x-1]+mMap[y][x]+mMap[y-1][x+1]
  if((word1 == "SAM" or word1 == "MAS") and (word2 == "SAM" or word2 == "MAS")):
    return 1
  return 0

mMap = common.ReadInput(4)

H = len(mMap)
W = len(mMap[0])

p1 = 0
p2 = 0
for y in range(H):
  for x in range(W):
    p1 += countXmas(mMap, x, y, W, H)
    p2 += countX(mMap, x, y, W, H)
print(p1)
print(p2)