import sqlite3


def create_table_alumni():
    conn = sqlite3.connect('students_list.db')

    cursor = conn.cursor()

    table_test = cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='students' ''').fetchall()

    if table_test == []:
        cursor.execute('''
            CREATE TABLE students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            ''')
        cursor.close()
        conn.commit()
        conn.close()
    else:
        cursor.close()
        conn.commit()
        conn.close()

def add_new_student(id, name, last_name):
    conn = sqlite3.connect('students_list.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO students (id, name, last_name) VALUES ({id}, '{name}', '{last_name}')
    ''')
    cursor.close()
    conn.commit()
    conn.close()

def fetch_student(name):
    conn = sqlite3.connect('students_list.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT * FROM students WHERE name='{name}'
    ''')
    for row in cursor:
        print(f'{row[0]} | {row[1]} {row[2]}')
    cursor.close()
    conn.close()



if __name__ == '__main__':
    create_table_alumni()
    add_new_student(1, 'Pedro', 'Ferenandez')
    add_new_student(2, 'Margarita', 'Gomez')
    add_new_student(3, 'Pedro', 'Martinez')
    add_new_student(4, 'Linda', 'Cadiz')
    add_new_student(6, 'Ramiro', 'Moreno')
    add_new_student(7, 'Galileo', 'Leibniz')
    add_new_student(8, 'Margaret', 'Hamillton')
    fetch_student('Pedro')
