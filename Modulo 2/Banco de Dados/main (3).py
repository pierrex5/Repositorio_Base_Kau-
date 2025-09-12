import sqlite3 as sq

escola = sq.connect('escola.db')

cursor = escola.cursor()

#cursor.execute('SELECT nome, nota FROM alunos')
#cursor.execute("SELECT * FROM alunos WHERE id = '3'")
cursor.execute("SELECT nome, nota FROM alunos WHERE turma = 'B'")


resultados = cursor.fetchall()


for alunos in resultados:
    print(alunos)