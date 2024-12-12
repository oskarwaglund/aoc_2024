import common

def reduce(dx, dy):
  div=2
  while div <= max(dx, dy):
    while dx%div==0 and dy%div ==0:
      dx//=div
      dy//=div
    div+=1
  return (dx, dy)

def inside(x, y, w, h):
  return x>=0 and x < w and y>= 0 and y<h

def calculateNode(a1, a2, w, h):
  dx = a1[0]-a2[0]
  dy = a1[1]-a2[1]
  n1 = (a1[0]+dx, a1[1]+dy)
  n2 = (a2[0]-dx, a2[1]-dy)
  res=[]
  if(inside(n1[0], n1[1],w,h)):
    res.append(n1)
  if(inside(n2[0], n2[1],w,h)):
    res.append(n2)
  return res

def calculateResonance(a1, a2,w,h):
  dx = a1[0]-a2[0]
  dy = a1[1]-a2[1]
  (dx, dy) = reduce(dx, dy)
  nodes=set()
  probe=a1
  while(inside(probe[0], probe[1], w, h)):
    nodes.add(probe)
    probe=(probe[0]-dx, probe[1]-dy)
  probe=a1
  while(inside(probe[0], probe[1], w, h)):
    nodes.add(probe)
    probe=(probe[0]+dx, probe[1]+dy)
  return nodes

def calculateNodes(ant, p2,w,h):
  nodes=set()
  for i in range(len(ant)-1):
    for j in range(i+1, len(ant)):
      if(p2):
        nodes.update(calculateResonance(ant[i], ant[j], w, h))
      else:
        nodes.update(calculateNode(ant[i], ant[j],w,h))
  return nodes

mmap=common.ReadInput(8)
w=len(mmap[0])
h=len(mmap)

antennas=dict()

for y in range(h):
  for x in range(w):
    c=mmap[y][x]
    if(c!='.'):
      if(not c in antennas):
        antennas[c] = []
      antennas[c].append((x,y))

nodes=set()
for a in antennas:
  nodes.update(calculateNodes(antennas[a], False, w, h))
print(len(nodes))

nodes=set()
for a in antennas:
  nodes.update(calculateNodes(antennas[a], True, w, h))
print(len(nodes))