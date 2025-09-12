Usuário = input("Seu nome para realizar e não ocorrer problemas de envio até sua moradia:")
Lanche_escolhido = []
Resposta = []

while Resposta != 0:
   Resposta = int(input(f"Bem vindo (a) {Usuário} \n 1-Pedido de lanche. \n 2-Lista de lanches. \n 3-remover pedidos . \n 0-Sair"))
   if Resposta == 1:
      lanche= input("Qual o lanche escolhido pelo Usuário?")
      Lanche_escolhido.append(lanche)
   
   elif Resposta == 2:
      print(Lanche_escolhido)
  
   elif Resposta == 3:
      lanche= input("Qual o lanche voce qer remover ?")
      Lanche_escolhido.remove(lanche)
  
print("Pedido realizado.")





