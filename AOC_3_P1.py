import string

with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')

low, high = list(zip(string.ascii_lowercase, range(1, 27))), list(
zip(string.ascii_uppercase, range(27, 53)))
chars = dict(low+high)

total = 0
for i in arr:
    c1, c2 = i[:len(i)//2], i[len(i)//2:]
    for j in c1:
        if j in c2:
            total += chars[j]
            break
print(total)