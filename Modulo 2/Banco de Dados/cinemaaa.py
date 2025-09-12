import sqlite3 as sq

cinema = sq.connect('cinema.db')

cursor = cinema.cursor()

#cursor.execute('SELECT titulo, genero FROM filmes ')
#cursor.execute("SELECT * FROM filmes WHERE titulo = 'Matrix'")
cursor.execute("SELECT titulo FROM filmes WHERE ano > 2010 ")


resultados = cursor.fetchall()


for cinema in resultados:
    print(cinema)