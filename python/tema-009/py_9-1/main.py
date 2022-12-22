import re


def main():

    countries = input('Please, type the name of countries that you know. \nSeparate each one with a comma\n')
    countriesList = sorted(set(re.sub(r',\s+', ",", countries).title().strip().split(',')))
    for elem in countriesList.copy():
        elem.strip()
        if elem == '' or elem == r",\s+":
            countriesList.remove(elem)
    print(', '.join(countriesList))

if __name__ == '__main__':
    main()

import re