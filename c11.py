import common
from collections import defaultdict

data=[int(a) for a in common.ReadInput(11)[0].split()]
count = defaultdict(int)
for d in data:
  count [d] += 1

for i in range(75):
  next=defaultdict(int)
  for stone, amount in count.items():
    if stone == 0:
      next[1] += amount
    elif len(str(stone)) % 2 == 0:
      s = str(stone)
      next[int(s[:len(s)//2])] += amount
      next[int(s[len(s)//2:])] += amount
    else:
      next[stone*2024] += amount
  count = next

  #P1
  if(i == 24):
    print(sum(count.values()))
#P2
print(sum(count.values()))
