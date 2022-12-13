with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')
total = 0
for i in arr:
    ran = i.split(',')
    ran[0] = ran[0].split('-')
    ran[1] = ran[1].split('-')
    set1 = set(range(int(ran[0][0]), int(ran[0][1])+1))
    set2 = set(range(int(ran[1][0]), int(ran[1][1])+1))
    final = set1.intersection(set2)
    if len(final) != 0:
        total += 1
print(total)