'''
Escreva um programa que solicite ao usuário um valor em metros e ofereça duas
opções: converter para centímetros ou para quilômetros. Dependendo da escolha do
usuário, o programa deverá chamar a função correspondente de conversão.
A função para converter metros em centímetros deve receber como parâmetro o valor
em metros e retornar o valor em centímetros. A função para converter metros em
quilômetros deve receber como parâmetro o valor em metros e retornar o valor em
quilômetros.
No programa principal, você deverá receber por input o valor em metros e a opção de
conversão, logo após, imprima o valor retornado pela função que o usuário escolher.
Centímetros = Metros * 100
Quilômetros = Metros/1000
'''

# Converte um valor em metros para centímetros.
def converter_cm(valor):
    return valor * 100

# Converte um valor em metros para quilômetros.
def converter_km(valor):
    return valor / 1000

# Obtém o valor em metros a ser convertido, convertendo a entrada para um número de ponto flutuante
valor = float(input("Informe o valor (em metros): "))

# Apresenta o menu de opções ao usuário
print("Menu:\n    1 - Converter em centímetros\n    2 - Converter em quilômetros")

# Obtém a escolha do usuário e a converte para um número inteiro
escolha = int(input("Escolha uma conversão: "))

# Estrutura condicional para realizar a conversão escolhida
if escolha == 1:
    # Chama a função para converter para centímetros e exibe o resultado
    print(f"{valor} metros = {converter_cm(valor)} centímetros")
elif escolha == 2:
    # Chama a função para converter para quilômetros e exibe o resultado
    print(f"{valor} metros = {converter_km(valor)} quilômetros")
else:
    # Exibe uma mensagem de erro caso a opção seja inválida
    print("Opção inválida!")