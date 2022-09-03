from functools import reduce

def getOdds(iterable):
    return list(filter(lambda x: x % 2 != 0, iterable))

def sumOdds(filtered):
    return reduce(lambda a, b: a + b, filtered)

def main():
    getList = list(range(1, 101))
    print(f'The original list is: {getList}')
    filteredList = getOdds(getList)
    print(f'The filtered list is: {filteredList}')
    solution = sumOdds(filteredList)
    print(f'The cumulative sum is: {solution}')

if __name__ == '__main__':
    main()

