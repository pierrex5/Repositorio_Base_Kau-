import sqlite3 as sq

empresa = sq.connect('empresa.db')

cursor = empresa.cursor()

#cursor.execute('SELECT nome, salario FROM funcionarios')
#cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
cursor.execute("SELECT nome, cargo FROM funcionarios WHERE departamento = 'TI'")

resultados = cursor.fetchall()


for funcionario in resultados:
    print(funcionario)