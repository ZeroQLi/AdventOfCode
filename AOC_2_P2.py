import regex as re
f = open('input.txt','r').readlines()

gSUM = 0

for i in f:
    i = i.split(': ')
    
    ID = re.findall(r"(\d+)",i[0])[0]

    red = [int(x) for x in re.findall(r"(\d+) \bred",i[1])]
    green = [int(x) for x in re.findall(r"(\d+) \bgreen",i[1])]
    blue = [int(x) for x in re.findall(r"(\d+) \bblue",i[1])]

    power  = max(red) * max(green) * max(blue)
    gSUM = gSUM+power
print(gSUM)