total_lugares = 20
lugares_disponiveis = total_lugares

print("Sistema de Reservas de Mesas - Restaurante")

while lugares_disponiveis > 0:
    nome = input("Nome da pessoa para a reserva: ")
    quantidade = input("Quantidade de pessoas para a reserva: ")

    
    if quantidade != "" and quantidade.isnumeric() and int(quantidade) > 0:
        quantidade_pessoas = int(quantidade)

        if quantidade_pessoas <= lugares_disponiveis:
            lugares_disponiveis -= quantidade_pessoas
            print(f"Reserva confirmada para {nome}, {quantidade_pessoas} pessoas.")
            print(f"Lugares restantes: {lugares_disponiveis}\n")
        else:
            print(f"Reserva recusada para {nome}. Não há lugares suficientes para {quantidade_pessoas} pessoas.")
            print(f"Lugares restantes: {lugares_disponiveis}\n")
    else:
        print("Por favor, informe uma quantidade válida (número inteiro maior que zero).\n")

print("Todas as mesas estão reservadas. Lotação esgotada!")
        