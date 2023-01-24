import csv, sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

with open('movies.csv', 'r') as d:
    reader = csv.reader(d, delimiter=";")
    next(reader)

    for row in reader:
        cursor.execute("INSERT INTO filmwho_movie VALUES (?,?,?,?,?,?)", row)

conn.commit()
conn.close()