import matplotlib.pyplot as plt

# Nomes dos jogadores de basquete e suas pontuações em um jogo
nomes_jogadores = ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo']
pontuacao = [30, 35, 28, 25]

# Cria o gráfico de barras
plt.bar(nomes_jogadores, pontuacao)

# Adiciona título e rótulos aos eixos
plt.title('Pontuação dos Jogadores de Basquete')
plt.xlabel('Nomes dos Jogadores')
plt.ylabel('Pontos no Jogo')

# Rotaciona os nomes para melhor visualização, se necessário
plt.xticks(rotation=45)

# Ajusta o layout para evitar que os rótulos sejam cortados
plt.tight_layout()

# Mostra o gráfico
plt.show()