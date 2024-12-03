import re

with open('input.txt', 'r') as f:
	output = f.read()
arr = re.findall(r'mul\(\d*,\d*\)', output)
total = 0
for x in arr:
	res = 1
	nums = [int(y) for y in re.findall(r'\d+', x)]
	for i in nums:
		res *= i
	total += res
print(total)