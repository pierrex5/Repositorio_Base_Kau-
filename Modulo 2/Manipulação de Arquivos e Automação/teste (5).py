import requests, bs4
res = requests.get('https://books.toscrape.com/index')
soup = bs4.BeautifulSoup(res . text, "html.parser")
type(soup)
soup.title.string #carrega o titulo da pagína
titulos_livros = [] #lista para amazenar od titulos dos livros
# Itera sobre cada livro encontrado
for livro in soup.select('.product_pod'):
    h3 = livro.find('h3')
#verifica se o h3 não possui atrinuto'class'
    if not h3.has_attr('class'):
       titulo = h3.a['title']
       titulos_livros.append(titulo)
print(soup.title.string)   #Carrega o titulo da pagina
print(titulos_livros)      #exibe os titulos......

if res.status_code == 200:
    print('Conexão realizada')

elif res.status_code == 403:
    print(f'Não autorizado')

elif res.status_code == 404:
    print(f'Não encontrado ou inexistente')

elif  res.status_code == 502:
    print(f"tempo de comunicação excedido")

elif  res.status_code == 503:
    print(f"tempo de comunicação excedido")

else:
    print(f"Beautifulsoup4 não existente.")




