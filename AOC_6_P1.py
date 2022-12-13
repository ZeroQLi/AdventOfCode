with open('input.txt', 'r') as f:
    output = f.read()

for i, s in enumerate(output):
    packet = output[i:i+4]
    if len(set(packet)) == len(packet):
        print(len(output[0:i+4]))
        break