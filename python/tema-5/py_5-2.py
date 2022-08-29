def check_number():
    print('Is your number a prime?')
    number = int(input('Please, type a natural number\n'))

    isPrime = (lambda num: 'Yes, {res} is prime'.format(res=num) if (number >= 0 and number // 1 == number and number % 2 != 0 and number != 1) or number == 2 else 'No, {res} isn\'t prime'.format(res=num))(number) 
    return isPrime
print(check_number())
print('by Favio')
