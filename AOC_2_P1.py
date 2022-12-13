score = {
    'X':1,
    'Y':2,
    'Z':3
}
with open('input.txt', 'r') as f:
    output = f.read()

arr = output.split('\n')

total = 0
for i in arr:
    k = score[i.split(' ')[1]] ## fetches the value of the last letter of the string
    i = i.replace(" ", "") # removes space
    if i == 'AX' or i == 'BY' or i == 'CZ': # draw
        total += 3 + k
    elif i == 'BX' or i == 'CY' or i == 'AZ': # loss
        total += 0 + k
    else: # win
        total += 6 + k
print(total)