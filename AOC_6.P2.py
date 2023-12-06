import regex as re
f = open('input.txt','r').readlines()

times = int(''.join(re.findall(r"\d+",f[0])))
recDist = int(''.join(re.findall(r"\d+",f[1])))

print(times,recDist)

total = 0
for i in range(0,times):
    distance = i*(times-i)
    if distance > recDist:
        total += 1
        
print("total values: ",total)