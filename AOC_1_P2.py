f = open("input.txt", "r")
input = f.read().split('\n')


input = [int(x) for x in input]

total = 0

for i in range(1, len(input)-2):
    k = input[i] + input[i+1] + input[i+2]
    s = input[i-1] + input[i] + input[i+1]
    if k > s:
        total += 1

print(total)
