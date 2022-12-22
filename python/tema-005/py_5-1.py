import math

def calculateArea(shape):
    triangle = lambda base, height: round(((base * height )/ 2), 2)

    circle = lambda radius: round((math.pi * (radius**2)), 2)  

    match shape:
        case '1':
            base = float(input('Type the base of your triangle\n'))
            height = float(input('Type the height of your triangle\n'))
            return triangle(base, height)
        case '2':
            radius = float(input('Type the radius of your circle\n'))
            area = circle(radius)
            return area
        case _:
            return calculateArea(input('You have selected an out boundary option. Please, try again (Type 1 or 2)\n'))

print('Area calculator')
shape = input('Please type 1 or 2.\n1 stands for triangle area.\n2 stands for a circle area.\n')
area = calculateArea(shape)
response = 'Your triangle\'s area is: {res}'.format(res = area)  if shape == '1' else 'Your circle\'s area is: {res}'.format(res = area)
print(response)
print('by Favio')
