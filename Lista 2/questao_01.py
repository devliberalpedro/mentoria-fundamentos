'''
Desenvolva um programa para ler a quantidade de pessoas de um grupo. Para cada integrante, informe o peso. O algorítmo deverá imprimir a média dos pesos e quantos estão acima de 80kg
'''

# Realizamos o input convertendo para o tipo inteiro, para facilitar a lógica do código. Lembrem-se que o input, por padrão, sem conversão, receberá uma string!
qtd_integrantes = int(input("Informe a quantidade de integrantes do grupo: "))
# Definimos uma variável para armazenar  a soma dos pesos e quantas pessoas estão acima de 80kg
# Inicializamos estas variáveis com o valor zero.
soma = acima = 0

# Nosso for irá repetir a quantidade de integrantes que informamos no input inicial
# A variãvel idx é um contador que começa em zero e será incrementado (+1) a cada repetição até chegar no valor da variável qtd_integrantes
for idx in range(qtd_integrantes):
    # A cada interação, somaremos o peso informado à soma dos pesos (na primeira interação, a soma iniciará com zero)
    peso = float(input(f"Informe o peso do {idx + 1}º integrante: "))
    soma += peso

    # Se o peso informado for maior que 80, incrementamos em 1 a variável acima (que inicia com zero na primeira repetição)
    if peso > 80:
        acima += 1

# O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
# O entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
print(f"A média de peso entre os {qtd_integrantes} integrantes é de {soma / qtd_integrantes}")
print(f"{acima} integrantes estão acima de 80kg")
