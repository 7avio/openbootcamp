age = int(input("Please, type your age...\n"))

response = 'Congrats. You\'re an adult. You can pass' if age>=18 else 'Sorry, you\'re underage. You can\'t pass'
print('{res}\nby Favio'.format(res = response))
