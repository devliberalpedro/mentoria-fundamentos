'''
Questão 05

Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor, deverá ser impressa a palavra EMPATE
'''

# Realizamos os inputs dos times 1 e 2 e seus respectivos gols. Apenas os inputs dos gols deverão ser convertidos para o tipo inteiro
time1 = input("Nome do 1º time: ")
gols1 = int(input("Quantos gols o 1º time marcou? "))

time2 = input("Nome do 2º time: ")
gols2 = int(input("Quantos gols o 2º time marcou? "))

# Se um time marcou mais gols que o outro, será o vencedor, caso não, será empate
if gols1 > gols2:
    # O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
    # o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
    print(f"O {time1} venceu!")
elif gols1 < gols2:
    print(f"O {time2} venceu!")
else:
    print("EMPATE")