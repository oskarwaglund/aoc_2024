import common

def canSolve(total, values, index, current, concatSupported):
  if(current>total):
    return False
  if(index==len(values)):
    return total==current
  if(index > 0 and concatSupported):
    n=int(str(current)+str(values[index]))
    if(canSolve(total, values, index+1, n, True)):
      return True
  return canSolve(total, values, index+1, current+values[index], concatSupported) or canSolve(total, values, index+1, current*values[index], concatSupported)

lines = common.ReadInput(7)
p1=0
p2=0
for l in lines:
  colonSplit = l.split(':')
  total=int(colonSplit[0])
  valueSplit = colonSplit[1].split()
  values=[int(a) for a in valueSplit]
  if(canSolve(total, values, 0, 0, False)):
    p1+=total
    p2+=total
  elif(canSolve(total, values, 0, 0, True)):
    p2+=total

print(p1)
print(p2)