nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

arquivo = open("caminho_do_arquivo.txt" , "a")
arquivo.write( nome + "|" + email + "\n")
arquivo.close()

