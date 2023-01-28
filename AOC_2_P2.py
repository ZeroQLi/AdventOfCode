f = open('input.txt', 'r')
input = f.read().split('\n')

h = 0
d = 0
a = 0

for i, j in enumerate(input):
    c, v = j.split(' ')
    v = int(v)
    match c:
        case 'forward':
            h += v
            d += v*a
        case 'down':
            a += v
        case 'up':
            a -= v

print(h*d)
