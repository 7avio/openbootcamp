import csv, sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

with open('BDirectors.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        cursor.execute("INSERT INTO filmwho_director VALUES (?,?,?,?,?)", row)

conn.commit()
conn.close()