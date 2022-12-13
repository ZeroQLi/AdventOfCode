with open('test.txt', 'r') as f:
    output = f.read()
arr = output.split('\n')


vis = len(arr[0]) + len(arr[-1])

for i, j in enumerate(arr[1:-1], 1):
    vis += 2
    for j, k in enumerate(j[1:-1], 1):
        if k < 