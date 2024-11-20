import database.conn as db


db.cursor.execute('SELECT * FROM users')

#obtem os resultados
rows = db.cursor.fetchall()
for row in rows:
    print(row)
