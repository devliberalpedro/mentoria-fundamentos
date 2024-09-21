'''
Um corretor quer analisar como foi sua venda no dia. Desenvolva um programa que receba a quantidade de apartamentos vendidos no dia e na sequência:

a) Implemente um vetor de números reais chamado areas, correspondente a área de cada um dos apartamentos vendidos (adicione as áreas no vetor);
b) Calcule e mostre na tela a soma das áreas;
c) O maior e o menor apartamento vendido.
'''

# Cria uma lista vazia para armazenar as áreas dos apartamentos vendidos
areas = []

# Solicita ao corretor o número total de apartamentos vendidos no dia
total_vendas = int(input("Total de vendas no dia: "))

# Loop para coletar as áreas de cada apartamento vendido
for idx in range(total_vendas):
    # Solicita a área do apartamento atual e a converte para um número de ponto flutuante (float)
    area = float(input(f"Informe a área do {idx + 1} apartamento: "))
    # Adiciona a área à lista 'areas'
    areas.append(area)

# Calcula e exibe a soma total das áreas dos apartamentos vendidos
print(f"A soma de todas as áreas é {sum(areas)}")

# Encontra e exibe a área do maior apartamento vendido
print(f"O maior apartamento tem {max(areas)}m² de área")

# Encontra e exibe a área do menor apartamento vendido
print(f"O menor apartamento tem {min(areas)}m² de área")