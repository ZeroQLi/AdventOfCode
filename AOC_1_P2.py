with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')
total, res = 0, []
for i in arr:
    if not i:
       res.append(total)
       total = 0
    else:
        total += int(i)
res.sort(reverse=True)
final = 0
for i in range(3):
    final += res[i]

print(final)
