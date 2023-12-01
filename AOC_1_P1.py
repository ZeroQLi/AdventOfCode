import re

f = open('input.txt','r').readlines()

total = 0
for i in f:
  noy = re.findall(r"(\d)",i)
  number = int(noy[0])*10 + int(noy[-1])
  total = total + number
print(total)