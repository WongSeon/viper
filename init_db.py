import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Michael Mcgee', 'Maybe ago organization wish anything suddenly road.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Tyler Hobbs', 'Environment study free many city religious property.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Angie Bruce', 'Political explain far soon add specific Mr foreign.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Matthew Hudson', 'Either animal treat game big interesting study hospital.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Kathryn Doyle', 'Own my assume contain sell recognize.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Anthony Nelson', 'Wind something whom stage live station.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Tracie Thomas', 'Think member he establish point foreign hand.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Susan Holland', 'Benefit campaign recognize plant benefit leave.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Kelly Moore', 'Late citizen bag public tonight.'))

cur.execute("INSERT INTO message (name, body) VALUES (?, ?)", ('Sara Mcdaniel', 'Open notice travel position property manager.'))

connection.commit()
connection.close()
