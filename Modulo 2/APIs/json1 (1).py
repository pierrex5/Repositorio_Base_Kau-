import json 

dados_json ='{ "Nome": "Ana", "idade":25,  "Cidade":"São paulo" }'     
dados_pyhton = json.loads(dados_json)   
print(dados_pyhton["Nome"])
print(dados_pyhton["idade"])



















