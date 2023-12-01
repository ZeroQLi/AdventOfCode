import regex as re

f = open('input.txt','r').readlines()

nums = {
  "one": 1,
  "two": 2,
  "three":3,
  "four":4,
  "five":5,
  "six":6,
  "seven":7,
  "eight":8,
  "nine": 9
}

total = 0

for i in f:
  number = 0
  noy = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)",i,overlapped=True)
  num1, num2 = noy[0], noy[-1]
  if num1.isalpha():
    number = nums[num1]*10
  else:
    number = int(num1)*10
  if num2.isalpha():
    number = number + nums[num2]
  else:
    number = number + int(num2)
  total = total + number
print(total)