import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 5

    print("=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número entre 1 e 100. Você tem 5 tentativas.")

    for tentativa in range(1, tentativas + 1):
        chute = int(input(f"Tentativa {tentativa}: Digite um número: "))

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} na tentativa {tentativa}.")
            break
        else:
            diferenca = abs(numero_secreto - chute)
            if diferenca <= 10:
                dica = "Quente! Está quase..."
            elif diferenca > 30:
                dica = "Frio! Tente um valor mais alto." if chute < numero_secreto else "Frio! Tente um valor mais baixo."
            else:
                dica = "Morno! Você está chegando perto."

            print(dica)

    else:
        print(f"Suas tentativas acabaram! O número era {numero_secreto}.")

# Executar o jogo
jogo_adivinhacao()















































    