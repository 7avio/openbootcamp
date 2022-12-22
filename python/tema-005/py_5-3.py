def is_leap():
    set_year = int(input('Please, type a four digit year\n'))
    is_leap = lambda year: '\nYes, {res} is a leap year'.format(res = year) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else '\nNo, {res} isn\'t a leap year'.format(res = year)
    return is_leap(set_year)
print(is_leap())
print('\nby Favio')
