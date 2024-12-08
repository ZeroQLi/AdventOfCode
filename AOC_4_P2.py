import re

with open('input.txt', 'r') as f:
	output = f.read()
arr = [x for x in output.split('\n')]
total = 0

max_col = len(arr[0])
max_row = len(arr)

for x in range(1, max_col - 1):
	for y in range(1, max_row - 1):
		if (arr[x][y] == 'A'):
			fdiag = ''.join(list((arr[x-1][y-1], arr[x][y], arr[x+1][y+1])))
			bdiag = ''.join(list((arr[x-1][y+1], arr[x][y], arr[x+1][y-1])))
			if ((fdiag == 'MAS' or fdiag == 'SAM') and (bdiag == 'MAS' or bdiag == 'SAM')):
				total += 1
print(total)
