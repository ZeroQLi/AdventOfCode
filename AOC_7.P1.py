f = open('test.txt', 'r').readlines()

labels=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

kind5, kind4, FullH, kind3, twoP, oneP, HC  = [],[],[],[],[],[],[]


for i in f:
    hand, bid = i.split(' ')

    uhand = set(hand)
    print(hand)

    if len(uhand) == 1:
        kind5.append(hand)
        continue

    if len(uhand) == 2:
        x = hand[0]
        if hand.count(x) == 4 or hand.count(x)== 1:
            kind4.append(hand)
            continue
        else:
            FullH.append(hand)
            continue

    if len(uhand) == 3:
        y = hand[0]
        if hand.count(y) == 3:
            kind3.append(hand)
            continue
        elif hand.count(y) == 2:
            twoP.append(hand)
            continue
        else:
            if hand.count(hand[1]) == 3:
                kind3.append(hand)
                continue
            else:
                twoP.append(hand)
                continue

    elif len(uhand) == 4:
        oneP.append(hand)
        continue

    elif len(uhand) == 5:
        HC.append(hand)
        continue  
types = list((kind5, kind4, FullH, kind3, twoP, oneP, HC))

for kind in types:
    if len(kind) == 1:
        print(kind)
    else:
        for i, j in enumerate(kind):
            print(i,j)
            if labels.index(j[0]) > labels.index(kind[i+1][0]):
                print(j)
                continue
