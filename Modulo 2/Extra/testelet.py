import flet as ft #👉 Importa o módulo flet com o apelido ft, que é usado para criar a interface gráfica.



def main(page: ft.Page): #👉 Define a função principal chamada main. Ela recebe um objeto page, que representa a tela da aplicação Flet.
    page.title = "Placar de Basquete Simples" #👉 Define a função principal chamada main. Ela recebe um objeto page, que representa a tela da aplicação Flet.

    pontos_a = ft.Text("0", size=40)
    pontos_b = ft.Text("0", size=40) #👉 Cria dois textos grandes (tamanho 40) que começam com "0", representando os pontos do Time A e Time B.

    def adicionar_ponto_a(e):
        pontos_a.value = str(int(pontos_a.value) + 1)
        page.update() # Função chamada quando clicamos no botão de adicionar ponto para o Time A:   Atualiza o valor na tela com page.update()

    def adicionar_ponto_b(e):
        pontos_b.value = str(int(pontos_b.value) + 1)
        page.update() #👉 Mesma lógica da função anterior, mas para o Time B.

    page.add(  #👉 Mesma lógica da função anterior, mas para o Time B.
        ft.Column([  #👉 Coloca os elementos organizados em coluna (um embaixo do outro).


            ft.Text("Time A", size=20),  
            pontos_a, #👉 Mostra a pontuação atual do Time A (aquele Text("0") que criamos lá em cima). 
            ft.ElevatedButton(text="+1 ponto A", on_click=adicionar_ponto_a), #👉 Cria um botão com o texto "+1 ponto A" que, ao ser clicado, chama a função adicionar_ponto_a.

            ft.Divider(), #👉 Cria uma linha divisória horizontal entre os dois times.  

            ft.Text("Time B", size=20),
            pontos_b,
            ft.ElevatedButton(text="+1 ponto B", on_click=adicionar_ponto_b),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20) #👉 Finaliza a coluna
    )

ft.app(target=main)
#👉 Chama a função main e inicia a aplicação Flet, com essa função como ponto de entrada.
