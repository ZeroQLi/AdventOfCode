import regex as re
test = open('input.txt','r').readlines()

symbols = ['#','$','*','&','/','@','%','+','-','=']

SUM = 0

for index, arr in enumerate(test):
    numbers = re.findall(r'\d+', arr)
    print(numbers)
    if index == 0:
        for num in numbers:
            x = re.search(rf"\b{num}\b", arr).start()
            if x == 0:
                for j in range(len(num)):
                    if test[index+1][j] in symbols or test[index+1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            elif x == len(arr)-len(num):
                for j in range(len(arr)-len(num),len(arr)):
                    if test[index+1][j] in symbols or test[index+1][j-1] in symbols or arr[j-1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            else:
                for j in range (x,x+len(num)):
                    if arr[j-1] in symbols or test[index+1][j-1] in symbols or test[index+1][j] in symbols or test[index+1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
    elif index == len(test)-1:
        for num in numbers:
            x = re.search(rf"\b{num}\b", arr).start()
            if x == 0:
                for j in range(len(num)):
                    if test[index-1][j] in symbols or test[index-1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            elif x == len(arr)-len(num):
                for j in range(len(arr)-len(num),len(arr)):
                    if test[index-1][j] in symbols or test[index-1][j-1] in symbols or arr[j-1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            else:
                for j in range (x,x+len(num)):
                    if arr[j-1] in symbols or test[index-1][j-1] in symbols or test[index-1][j] in symbols or test[index-1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
    else:
        for num in numbers:
            x = re.search(rf"\b{num}\b", arr).start()
            if x == 0:
                for j in range(len(num)):
                    if test[index-1][j] in symbols or test[index-1][j+1] in symbols or arr[j+1] in symbols or test[index+1][j] in symbols or test[index+1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            elif x == len(arr)-len(num):
                for j in range(len(arr)-len(num),len(arr)):
                    if test[index-1][j] in symbols or test[index-1][j-1] in symbols or arr[j-1] in symbols or test[index+1][j] in symbols or test[index+1][j-1] in symbols or arr[j-1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
            else:
                for j in range (x,x+len(num)):
                    if arr[j-1] in symbols or test[index-1][j-1] in symbols or test[index-1][j] in symbols or test[index-1][j+1] in symbols or arr[j+1] in symbols or arr[j-1] in symbols or test[index+1][j-1] in symbols or test[index+1][j] in symbols or test[index+1][j+1] in symbols or arr[j+1] in symbols:
                        SUM = SUM+int(num)
                        print(num)
                        break
print(SUM)
    #for i, j in enumerate(arr):