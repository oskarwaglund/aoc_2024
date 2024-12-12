import common
from functools import cmp_to_key

def compare(a, b, order):
  if [a,b] in order:
    return -1
  elif [b,a] in order:
    return 1
  return 0

input = common.ReadInput(5)

parsingOrder=True
order = []
p1=p2=0
for l in input:
  if(len(l) == 0):
    parsingOrder = False
    continue
  if(parsingOrder):
    order.append([int(a) for a in l.split('|')])
  else:
    pages = [int(a) for a in l.split(',')]
    sortedPages = sorted(pages, key=cmp_to_key(lambda a, b: compare(a, b, order)))
    if(sortedPages == pages):
      p1 += pages[len(pages)//2]
    else:
      p2 += sortedPages[len(pages)//2]

print(p1)
print(p2)