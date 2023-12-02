import regex as re
f = open('input.txt','r').readlines()

gSUM = 0

Tred , Tgreen, Tblue = 12, 13, 14
red, green, blue = 0, 0, 0

for i in f:
    i = i.split(': ')
    
    ID = re.findall(r"(\d+)",i[0])[0]

    red = [int(x) for x in re.findall(r"(\d+) \bred",i[1])]
    green = [int(x) for x in re.findall(r"(\d+) \bgreen",i[1])]
    blue = [int(x) for x in re.findall(r"(\d+) \bblue",i[1])]

    if Tred < max(red) or Tgreen < max(green) or Tblue < max(blue):
        continue
    gSUM = gSUM+int(ID)
print(gSUM)
    