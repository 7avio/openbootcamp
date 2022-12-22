

from os import name


contactInfo = {
    'name': 'Tony',
    'last_name': 'Stark',
    'age': 50,
    'email': 'imironmanofficial@fakemail.avgs',
    'telephone': 2129704133,
    'marital_status': True,
    'childrens_status': True,
    'friends_list': ['Bruce Banner', 'Steven Rogers', 'Peter Parker'],
    'movies_watched': {
        1: 'Alien',
        2: 'Star Wars',
    }
}

text = '\nSubject A:\nFull name: {name} {last_name} ({age}).\nemail: {email} ... Contact number: {telephone}\nIs the subject married?: {marital_status}... Does the subject have kids?: {childrens_status}\nRelevant contact: {friends_list[0]}, {friends_list[1]}, {friends_list[2]}\nFavorite movies: {movies_watched[1]}, {movies_watched[2]}  '.format(**contactInfo)

print(text)
print('\nBy Favio')