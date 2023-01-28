f = open("input.txt", "r")
input = f.read().split('\n')


total = 0
print(input)
for i, j in enumerate(input[1:], 1):
    if int(j) > int(input[i-1]):
        total += 1
print(total)