import string

with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')

low, high = list(zip(string.ascii_lowercase, range(1, 27))), list(
zip(string.ascii_uppercase, range(27, 53)))
chars = dict(low+high)

def split(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def check(arr):
    score = 0
    for str in arr:
        for i in str:
            if i in arr[1] and i in arr[2]:
                score += chars[i]
                return score
total = 0
for group in split(arr, 3):
    total += check(group)

print(total)