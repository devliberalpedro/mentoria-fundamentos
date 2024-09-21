'''
Faça um programa que receba um valor em horas e dê duas opções ao usuário, converter em minutos ou em segundos. A partir da escolha do usuário, o programa deverá chamar a função específica de conversão.

- A função para converter horas em minutos deverá receber como parâmetro a hora e retornar o valor em minutos.
- A função para converter horas em segundos deverá receber como parâmetro a hora e retornar o valor em segundos.

No programa principal imprima o valor retornado pela função.
'''

# Define funções para realizar as conversões
def converter_minutos(horas):
    # Converte um valor em horas para minutos
    return horas * 60

def converter_segundos(horas):
    # Converte um valor em horas para segundos
    return horas * 3600

# Obtém a entrada do usuário para o valor em horas
horas = int(input("Informe uma valor de horas: "))

# Cria o menu de opções
menu = ["Menu:", "1 - Converter em minutos", "2 - Converter em segundos"]

# Imprime o menu na tela
for idx in menu:
    print(idx)

# Obtém a escolha do usuário para a conversão
escolha = int(input("Qual conversão deseja? "))

# Realiza a conversão e imprime o resultado de acordo com a escolha do usuário
if escolha == 1:
    convertido = converter_minutos(horas)
    print(f"O valor de {horas} horas convertidas em minutos: {convertido} minutos")
elif escolha == 2:
    convertido = converter_segundos(horas)
    print(f"O valor de {horas} horas convertidas em segundos: {convertido} segundos")
else:
    print("Valor inválido!")