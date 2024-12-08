import re

with open('input.txt', 'r') as f:
	output = f.read()
arr = [x for x in output.split('\n')]
total = 0

max_col = len(arr[0])
max_row = len(arr)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(arr[y][x])
        rows[y].append(arr[y][x])
        fdiag[x+y].append(arr[y][x])
        bdiag[x-y-min_bdiag].append(arr[y][x])
cols = [''.join(x) for x in cols]
rows = [''.join(x) for x in rows]
fdiag = [''.join(x) for x in fdiag]
bdiag = [''.join(x) for x in bdiag]

for i in range(max_row):
	#print(re.findall('XMAS', cols[i]) + re.findall('SAMX', cols[i]))
	#print(re.findall('XMAS', rows[i]) + re.findall('SAMX', rows[i]))

	total += len(re.findall('XMAS', cols[i])) + len(re.findall('SAMX', cols[i]))
	total += len(re.findall('XMAS', rows[i])) + len(re.findall('SAMX', rows[i]))

for i in range(len(fdiag)):
	#print(re.findall('XMAS', fdiag[i]) + re.findall('SAMX', fdiag[i]))
	#print(re.findall('XMAS', bdiag[i]) + re.findall('SAMX', bdiag[i]))
	
	total += len(re.findall('XMAS', fdiag[i])) + len(re.findall('SAMX', fdiag[i]))
	total += len(re.findall('XMAS', bdiag[i])) + len(re.findall('SAMX', bdiag[i]))


print(total)
