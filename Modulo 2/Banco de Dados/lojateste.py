import sqlite3 as sq

loja = sq.connect('loja.db')

cursor = loja.cursor()

#cursor.execute('SELECT produto, cliente FROM vendas ')
#cursor.execute("SELECT * FROM vendas WHERE cliente = 'João'")
cursor.execute("SELECT produto FROM vendas WHERE preco_unitario > 50 ")


resultados = cursor.fetchall()


for loja in resultados:
    print(loja)