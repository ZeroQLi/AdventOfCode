with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')
total, res =0, []
for i in arr:
    if i == '':
       res.append(total) 
       total = 0
    else:
        total += int(i)
print(max(res))
