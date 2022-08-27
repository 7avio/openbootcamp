import math

min = int(input('Please, type a real number for minimum edge\n'))
max = int(input('Please, type a real number for maximum edge\n'))

groupNums = []
groupNums.append(min)
groupNums.append(max)

sortedNums = sorted(groupNums)

for number in range(sortedNums[0], sortedNums[1]):
    isOdd = number % 2 != 0
    print('{num} is odd'.format(num=number)) if isOdd else print(number)

print('by Favio')