import json

dados = {
    "nome": "Ricardo",
    "idade": 15,
    "email": "Ricardo@email.com",
    "ativo": True,
    "Interesses": ["phyton", "Dados" , "Machine Learning"]
}

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False,indent=4)























