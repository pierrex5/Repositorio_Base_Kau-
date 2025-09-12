NOME = print(input("Digite seu nome: "))
alt = float(input("Digita sua altura: "))
kg = float(input("digite seu peso:  "))
IMC= kg / (alt*alt)                     
if IMC <= 18.4:
    print("Seu peso está abaixo. ")
elif IMC >=18.5 and IMC <= 24.9:
    print("Seu peso está normal. ")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Seu peso está acima. ")
elif IMC >= 30.0 and IMC <= 34.9:
    print("o paciente está com obesidade Grau 1.")
elif IMC >= 35.0 and IMC<=39.9:
    print("o paciente está com obesidade Grau 2")
else:
    print("o paciente está com obesidade Grau 3(Mórbida")
print("------------------------------------------------")

