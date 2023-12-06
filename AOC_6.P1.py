import regex as re
f = open('input.txt','r').readlines()

times = [int(x) for x in re.findall(r"\d+",f[0])]
distances = [int(x) for x in re.findall(r"\d+",f[1])]

records = list(zip(times,distances))

total = 1
for time, dist in records:
    no = 0
    for i in range(0,time+1):
        distance = i*(time-i)
        if distance > dist:
            no += 1
    total *= no
print(total)