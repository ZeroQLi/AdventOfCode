with open('input.txt', 'r') as f:
	output = f.read()
arr = [x.split() for x in output.split('\n')]
total = 0

for i in range(len(arr)):
	check = [int(x) for x in arr[i]]
	zipped = list(zip(check, check[1:]))
	
	res_adjacent = all(abs(i-j) >= 1 and abs(i-j) <= 3 for i, j in zipped)

	res_same = all(i > j for i, j in zipped) or all(i < j for i, j in zipped)
	if (res_adjacent and res_same):
		total += 1
print(total)