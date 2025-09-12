def analisar_texto(texto):
    texto = texto.lower()
    
    vogais = "aeiouáàâãéèêíïóôõöúü"
    
    import string
    palavras = texto.split()            
    palavras = [p.strip(string.punctuation) for p in palavras if p.strip(string.punctuation) != '']
    
    total_palavras = len(palavras)
    

    palavra_mais_longa = max(palavras, key=len) if palavras else ""
    
    contador_vogais = 0
    contador_consoantes = 0
    for char in texto:
        if char.isalpha():
            if char in vogais:
                contador_vogais += 1
            else:       
                contador_consoantes += 1
    
    frequencia_palavras = {}
    for p in palavras:
        frequencia_palavras[p] = frequencia_palavras.get(p, 0) + 1
    

    print(f"Total de palavras: {total_palavras}")
    print(f'Palavra mais longa: "{palavra_mais_longa}"')
    print(f"Vogais: {contador_vogais} | Consoantes: {contador_consoantes}")
    print("\nFrequência de palavras:")
    for palavra, freq in sorted(frequencia_palavras.items()):
        print(f"{palavra}: {freq}")

texto_usuario = input("Digite ou cole seu texto:\n")
analisar_texto(texto_usuario)
