f = open('input.txt', 'r')
input = f.read().split('\n')



arr = []
g =''
e= ''
for i in range(len(input[0])):
    digit = []
    for k, j in enumerate(input):
        digit.append(j[i])
    zero = digit.count('0')
    one = digit.count('1')
    if zero > one:
        g+='0'
        e+='1'
    else:
        g += '1'
        e += '0'
print(int(e, 2)* int(g, 2))
