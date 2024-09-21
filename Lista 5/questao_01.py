'''
Desenvolva um programa que possua um vetor de 10 números inteiros. Após o
usuário inserir os valores, mostre quantos desses números são maiores, menores e
iguais ao primeiro elemento do vetor
'''

# Cria uma lista vazia para armazenar os números
numeros = []

# Inicializa contadores para números maiores e menores que o primeiro elemento
maiores = menores = 0

# Loop para receber 10 valores do usuário
for idx in range(10):
    # Solicita ao usuário que insira um valor e o converte para inteiro
    valor = int(input(f"Insira o {idx +1}º valor: "))
    
    # Adiciona o valor à lista
    numeros.append(valor)

    # Compara o valor com o primeiro elemento da lista, mas apenas a partir do segundo elemento inserido
    if idx > 0:  # Ignora a primeira comparação, pois o primeiro elemento é comparado consigo mesmo
        if valor > numeros[0]:
            maiores += 1  # Incrementa o contador de maiores se o valor for maior que o primeiro
        elif valor < numeros[0]:
            menores += 1  # Incrementa o contador de menores se o valor for menor que o primeiro

# Exibe o primeiro valor da lista e quantas vezes ele se repete na lista
print(f"O primeiro valor da lista é {numeros[0]} e ele se repete {numeros.count(numeros[0])} ")

# Exibe a quantidade de números maiores que o primeiro
print(f"Existem {maiores} números maiores que o primeiro da lista")

# Exibe a quantidade de números menores que o primeiro
print(f"Existem {menores} números menores que o primeiro da lista")