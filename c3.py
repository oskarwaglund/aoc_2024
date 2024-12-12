import common
import re
lines = common.ReadInput(3)

p1 = 0
p2 = 0
enabled = True
for l in lines:
  ops = re.findall("(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", l)
  for op in ops:
    if(op == "do()"):
      enabled = True
    elif(op == "don't()"):
      enabled = False
    else:
      values = op.replace("mul(", "").replace(",", " ").replace(")", "").split()
      product = int(values[0])*int(values[1])
      p1 += product
      p2 += product if enabled else 0

print(p1)
print(p2)
