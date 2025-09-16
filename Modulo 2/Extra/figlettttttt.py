import matplotlib.pyplot as plt

# Dados de exemplo
jogadores = ['LeBron James', 'Stephen Curry', 'Giannis Antetokounmpo', 'Kevin Durant']
pontos = [28, 32, 30, 27]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(jogadores, pontos, color='orange')

# Título e rótulos
plt.title('Pontuação por Jogo - Temporada 2024/25', fontsize=16)
plt.xlabel('Jogadores')
plt.ylabel('Pontos por jogo')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar o gráfico
plt.tight_layout()
plt.show()
