'''
Faça  um  programa  que  leia  uma  quantidade  indeterminada  de  números  positivos  e  conte  
quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de 
dados deverá terminar quando for lido um número negativo.
'''

# Inicializa contadores para cada intervalo e um valor inicial para o prompt
intervalo_01 = intervalo_02 = intervalo_03 = intervalo_04 = 0
valor = 1000

# Loop infinito para coletar valores até o usuário digitar um número negativo
while True:
    # Solicita ao usuário um valor inteiro e positivo
    valor = int(input("Informe um valor inteiro e positivo: "))

    # Se o valor for negativo, encerra o loop
    if valor < 0:
        break
    # Verifica em qual intervalo o valor se encaixa e incrementa o contador correspondente
    elif 0 <= valor <= 25:
        #intervalo_01 += 1
        intervalo_01 = intervalo_01 +1 #contador
    elif 26 <= valor <= 50:
        intervalo_02 += 1
    elif 51 <= valor <= 75:
        intervalo_03 += 1
    elif 76 <= valor <= 100:
        intervalo_04 += 1

# Imprime a quantidade de valores em cada intervalo
print(f"Valores entre [0-25]: {intervalo_01}")
print(f"Valores entre [26-50]: {intervalo_02}")
print(f"Valores entre [51-75]: {intervalo_03}")
print(f"Valores entre [76-100]: {intervalo_04}")