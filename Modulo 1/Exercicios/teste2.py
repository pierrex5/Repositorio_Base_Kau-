try:
    num_dolar = float(input("Digite o valor em Dólar: "))
    num_real = float(input("Digite o valor em Real: "))

    conversao_real = num_dolar / 5.64
    conversao_dolar = num_real * 5.64

    

    print(f"Seu Real convertido para Dólar é: ${conversao_real:.2f}")

    print(f"Seu Dólar convertido para Real é: R${conversao_dolar:.2f}")



except:
    print("Erro no valor. ")
