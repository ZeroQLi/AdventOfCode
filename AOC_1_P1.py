with open('input.txt', 'r') as f:
	output = f.read()
arr = output.split('\n')
loc1 = list(arr)
loc2 = list(arr)
total = 0

for i in range (len(arr)):
	loc1[i] = int(arr[i].split()[0])
	loc2[i] = int(arr[i].split()[1])
loc1.sort()
loc2.sort()

for i in range(len(arr)):
	total += max(loc1[i], loc2[i]) - min(loc1[i], loc2[i])
print(total)