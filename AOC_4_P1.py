import regex as re
f = open('input.txt','r').readlines()


total = 0

gSUM = 0
for i in f:
    s = i.split(' | ')
    winning = s[0].split(': ')
    cardNUM = [int(s) for s in winning[0].split() if s.isdigit()][0]
    winningNUMS = [int(s) for s in winning[1].split() if s.isdigit()]
    
    numbers = [int(s) for s in s[1].split() if s.isdigit()]
    print(cardNUM, winningNUMS, numbers)
    for j in numbers:
        if j in winningNUMS:
            print(j)
            if total == 0:
                total = 1
            else:
                total *= 2
    print('total for card',cardNUM,':',total)
    gSUM += total
    total=0
print(gSUM)