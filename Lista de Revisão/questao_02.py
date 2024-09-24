'''
Faça um programa que leia os modelos de cinco carro e salve em uma lista. Crie uma outra 
lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com 
um litro de combustível. Calcule e mostre: a) O modelo mais econômico b) Quantos litros cada carro consome para percorrer 1000km e quanto isto custará (considere 
o litro gasolina ao custo de R5,59)
'''

# Lista para armazenar os modelos dos carros
carros = []
# Lista para armazenar o consumo (km/l) de cada carro
consumos = []
# Preço do litro de gasolina
preco_gas = 6.00

# Loop para coletar dados de 5 carros
for idx in range(5):
    # Solicita o modelo do carro e adiciona à lista
    modelo_carro = input(f"Informe o modelo do {idx + 1}º carro: ")
    carros.append(modelo_carro)

    # Solicita o consumo do carro e adiciona à lista
    consumo_carro = float(input(f"Informe o consumo do {idx + 1}º carro: "))
    consumos.append(consumo_carro)

# Encontra o índice do carro mais econômico (maior consumo)
indice_mais_economico = consumos.index(max(consumos))
# Imprime o modelo do carro mais econômico
print(f"\n>> O carro mais econômico é o {carros[indice_mais_economico]}")

# Loop para calcular o consumo e custo para 1000km de cada carro
for idx in range(5):
    # Calcula o consumo para 1000km
    consumo_1000 = (1000 / consumos[idx])
    # Calcula o custo para 1000km
    custo_1000 = consumo_1000 * preco_gas

    # Imprime os resultados formatados
    print(f"- O {carros[idx]} consome {consumo_1000:.2f}l para percorrer 1000km ao custo total de R${custo_1000:.2f}")