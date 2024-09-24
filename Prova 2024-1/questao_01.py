'''
Um gerente de uma loja de eletrônicos deseja analisar o desempenho de vendas de
televisores ao longo de um dia. Desenvolva um programa que solicite ao usuário a
quantidade de televisores vendidos no dia e, em seguida:
a) Declare um vetor chamado "tamanhos", correspondente ao tamanho de cada um
dos televisores vendidos (adicione os tamanhos no vetor);
b) Calcule e mostre na tela a média dos tamanhos dos televisores vendidos;
c) Exiba qual foi o maior e o menor televisor vendido.
'''

# Lista para armazenar os tamanhos dos televisores
tamanhos = []

# Solicita ao usuário a quantidade de televisores vendidos e converte a entrada para um número inteiro
qtd_vendas = int(input("Quantidade de televisores foram vendidos: "))

# Itera sobre o número de televisores vendidos
for idx in range(qtd_vendas):
    # Solicita ao usuário o tamanho do televisor e converte a entrada para um número inteiro
    tv = int(input(f"Informe o tamanho do {idx + 1}º televisor: "))
    # Adiciona o tamanho do televisor à lista de tamanhos
    tamanhos.append(tv)

# Calcula a média dos tamanhos dividindo a soma dos tamanhos pela quantidade de televisores
media = sum(tamanhos) / qtd_vendas

# Imprime os resultados na tela, formatando a saída para melhor visualização
print(f"A média de tamanhos dos televisores foi de {media:.2f} polegadas.")
print(f"O maior tamanho foi de {max(tamanhos)} polegadas.")
print(f"O menor tamanho foi de {min(tamanhos)} polegadas.")