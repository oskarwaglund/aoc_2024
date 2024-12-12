import common

def isSafe(items):
  diffs = [(items[i]-items[i+1]) for i in range(len(items)-1)]
  return all(i >= 1 and i <= 3 for i in diffs) or all(i <= -1 and i >= -3 for i in diffs)

def isSafeP2(items):
  for i in range(len(items)):
    if(isSafe([x for j, x in enumerate(items) if j != i])):
      return True
  return isSafe(items)

lines = common.ReadInput(2)

p1 = 0
p2 = 0
for l in lines:
  items = [int(i) for i in l.split()]
  if(isSafe(items)):
    p1 += 1
  if(isSafeP2(items)):
    p2 += 1

print(p1)
print(p2)