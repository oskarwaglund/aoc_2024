import common
import copy

def checksum(diskMap):
  checksum = 0
  for i, c in diskMap.items():
    checksum += i*c if c >= 0 else 0
  return checksum

data = common.ReadInput(9)[0]

diskMap = dict()
fileMap = dict()
fileId = 0
blockIndex = 0
firstFree = -1
lastBlock = 0
lastFileId = 0
for i, c in enumerate(data):
  length=int(c)
  if i%2 == 0:
    lastFileId = fileId
    fileMap[fileId] = (blockIndex, length)
    for j in range(blockIndex, blockIndex+length):
      diskMap[j] = fileId
    lastBlock = j
    fileId += 1
  else:
    for j in range(blockIndex, blockIndex+length):
      diskMap[j] = -1
      if firstFree == -1:
        firstFree = j
  blockIndex += length

p1DiskMap = copy.deepcopy(diskMap)
#p1
while firstFree < lastBlock:
  p1DiskMap[firstFree] = p1DiskMap[lastBlock]
  p1DiskMap[lastBlock] = -1
  while p1DiskMap[firstFree] != -1 and firstFree in p1DiskMap:
    firstFree += 1
  while p1DiskMap[lastBlock] == -1:
    lastBlock -= 1

print(checksum(p1DiskMap))

#p2
gapMap = dict() #Points to where a gap search should start (value) for a given length (key)
fileId = lastFileId
while fileId >= 0:
  (fileStart, fileLength) = fileMap[fileId]
  #Find a place where the file fits if any
  newIndex = 0
  if fileLength in gapMap:
    newIndex = gapMap[fileLength]
  while newIndex < fileStart:
    #Find an empty block
    while diskMap[newIndex] != -1 and newIndex < fileStart:
      newIndex += 1
    if newIndex >= fileStart:
      break
    #Does it fit?
    fits = True
    for i in range(newIndex, newIndex+fileLength):
      if diskMap[i] >= 0:
        fits = False
        break
    if fits:
      gapMap[fileLength] = newIndex
      for i in range(newIndex, newIndex+fileLength):
        diskMap[i] = fileId
      for i in range(fileStart, fileStart+fileLength):
        diskMap[i] = -1
      assert fileStart > newIndex
      fileMap[fileId] = (newIndex, fileLength)
      break
    else:
      while diskMap[newIndex] == -1:
        newIndex += 1

  fileId -= 1

print(checksum(diskMap))
