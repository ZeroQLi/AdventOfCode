f = open('input.txt', 'r')
input = f.read().split('\n')

h = 0
d = 0

for i, j in enumerate(input):
    c, v = j.split(' ')
    v = int(v)
    match c:
        case 'forward':
            h += v
        case 'down':
            d += v
        case 'up':
            d -= v

print(h*d)