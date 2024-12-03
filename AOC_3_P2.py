import re

with open('input.txt', 'r') as f:
	output = f.read()
split = re.split(r"(don't\(\))|(do\(\))", output)
split = [x for x in split if x is not None]

enabled = True
total = 0

for i in split:
	if (enabled):
		if (i == "don't()"):
			enabled = False
		arr = re.findall(r'mul\(\d*,\d*\)', i)
		for x in arr:
			res = 1
			nums = [int(y) for y in re.findall(r'\d+', x)]
			total += nums[0] * nums[1]

	if (i == "do()"):
			enabled = True
print(total)