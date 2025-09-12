lista_tarefas = []
def adicionar():
    global Nome
    Nome = input("Qual seu nome: ")
    tarefa = input (f"Quais tarefas o {Nome} gostaria de adicionar?.")
def mostrar_lista():
    print(lista_tarefas)
Resposta = 5

while Resposta != 0:

    Resposta = int(input(f" :  \n 1-:Adicionar   \n 2- Mostratr a lista. \n 3- Varrer a casa. \n 0 - Limpar o banheiro."))

    if Resposta == 1 :
        adicionar()
    elif Resposta == 2 :
        mostrar_lista()

      

    elif Resposta == 3 :        
        
        print(f"O {Nome} varreu a a casa")



        excluir_compras = int (input("O que deseja remover da lista de :"))
        Tarefas_realizadas.remove(lista_tarefas)

        print (f"Você removeu com a tarefa {Nome}! ")
        print (Tarefas_realizadas)