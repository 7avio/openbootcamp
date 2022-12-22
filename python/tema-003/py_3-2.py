import math

#Pide peso en KG
print('Calculate your Body Mass Index (BMI)\n')
weightInKg = float(input('Please, insert your weight (kgms):\n'))
heightInM = float(input('Please, insert your height (m):\n'))
bmiCalculus = round((weightInKg/(math.pow(heightInM, 2))), 2)
response = '\nYour BMI is: {bmi:.2f}\n\nBy Favio'.format(bmi=bmiCalculus)

print(response)
