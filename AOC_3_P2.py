f = open('input.txt', 'r')
input = f.read().split('\n')

#incomplete

shallow = input.copy()

arr = []
raa = []

o = 0
c = 0

for i in range(len(input[0])):

    digit = []
    print(input)
    for k, j in enumerate(input):
        digit.append(j[i])
    zero = digit.count('0')
    one = digit.count('1')
    print(zero, one)
    if zero > one:
        arr = [k for k in input if k[i:].startswith('0')]
        input = [x for x in input if x in arr]
    else:
        arr = [k for k in input if k[i:].startswith('1')]
        input = [x for x in input if x in arr]

print(input)
