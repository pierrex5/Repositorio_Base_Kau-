import requests
url = "http://172.25.253.124:5000/alunos"
# 1️Exibir o código de status de uma requisição GET
res_get = requests.get(url)
print(f"Código de status do GET inicial: {res_get.status_code}")
# Adicionar seus dados via POST
dados = {
    "nome": "Kauã Pierre",
    "email": "kauapierree@gmail.com"
}
res_post = requests.post(url, json=dados)  # pode usar data=dados se o servidor não aceitar JSON
print(f"Código de status do POST: {res_post.status_code}")
print(f"Resposta do POST: {res_post.json}")

#  Visualizar os dados submetidos via GET
res_get_final = requests.get(url)
print("Dados após POST:")
print(res_get_final.json())