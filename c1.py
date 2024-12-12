import common
lines = common.ReadInput(1)

l1 = []
l2 = []

for l in lines:
  items = l.split()
  l1.append(int(items[0]))
  l2.append(int(items[1]))

l1.sort()
l2.sort()

p1 = 0
p2 = 0
for i in range(len(l1)):
  p1 += abs(l1[i]-l2[i])
  p2 += l1[i] * l2.count(l1[i])

print(p1)
print(p2)

