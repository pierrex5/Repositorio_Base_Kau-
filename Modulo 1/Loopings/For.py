total = 0
maior = 0
for i in range(1, 6):
    p = int(input(f"Participantes do dia {i}: "))
    total += p
    if p > maior:
        maior = p
print(f"Total: {total}\nMédia: {total/5:.2f}\nMaior: {maior}")
       


