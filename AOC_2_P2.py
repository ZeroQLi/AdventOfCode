A = {
    'X':3,
    'Y':1,
    'Z':2
}
B = {
    'X':1,
    'Y':2,
    'Z':3
}

C = {
    'X':2,
    'Y':3,
    'Z':1
}
with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')
total = 0
for i in arr:
    i = i.replace(" ", "")
    j = i[0]
    k = i[1]   
    if k == 'X':
        total += 0 + locals()[j][k]
    elif k == 'Z':
        total += 6 + locals()[j][k]
    else:
        total += 3 + locals()[j][k]
print(total)