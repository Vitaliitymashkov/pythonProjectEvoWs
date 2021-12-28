import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO users (name) VALUES (?)",
#             ('test_name_1',)
#             )
#
# cur.execute("INSERT INTO users (name) VALUES (?)",
#             ('Second_name',)
#             )

connection.commit()
connection.close()
