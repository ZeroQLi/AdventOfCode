with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n\n')
ship, com = arr[0].split('\n'), arr[1].split('\n')

cols = int(ship[-1][-1-1])

simp = dict({x: '' for x in range(1, cols+1)})

ship.pop(-1)
for i in reversed(ship):
    i = i.split(' ')
    lum = 1
    space = 0
    for j in i:
        if space == 4:
            lum += 1
            space = 0
        if j == '':
            space += 1
            continue
        j = j.replace('[', '').replace(']', '')
        if j.isalpha():
            simp[lum] += j
            lum += 1

wl = set(' 1234567890')
te = 10
for a in com:
    te += 1
    a = ''.join(filter(wl.__contains__, a))
    a = list(filter(None, a.split(' ')))
    a = [int(x) for x in a]
    for m in range(a[0]):
        simp[a[2]] = simp[a[2]] + simp[a[1]][-1]
        simp[a[1]] = simp[a[1]][:-1]

for i in simp:
    print(simp[i][-1], end='')
    

