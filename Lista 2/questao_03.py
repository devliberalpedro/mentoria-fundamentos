'''
Faça um algorítmo que receba idade de 6 pessoas. Por fim, o algirítmo deve informar:

- Quantas idades foram lidas;
- maior idade;
- menor idade;
- média das idades 
'''

# Teremos variáveis para armazenar a soma das idades, calcular a média das idades, contar quantas idades foram lidas
# quantas pessoas são maior de idade e também menor de idade. Inicializamos todas com zero.
soma_idades = media = idades_lidas = menores = maiores = 0 

# Nosso for irá repetir por 6 ocasiões
# A variãvel idx é um contador que começa em zero e será incrementado (+1) a cada repetição até chegar no valor seis
for idx in range(6):
    # Também podemos usar a formatação no input. Neste caso, usamos para imprimir se estamos pedindo a 1ª, 2ª, ... , 6ª idade.
    # Colocamos idx + 1 para informar qual idade coletamos por o idx inicia em zero, como citado antes do for
    idade = int(input(f"Informe a {idx + 1}ª idade: "))

    # Verificamos se a idade inserida é maior do que zero, evitando que o programa use valores negativos ou zero em seus cálculos, criando um erro
    # Somente se a idade for maior que zero, incrementamos a soma da idade, a quantidade de idades lidas e verificamos se é maior ou menor de idade
    if idade > 0:
        soma_idades += idade
        idades_lidas += 1

        # Vreificamos se a pessoa é maior ou menor de idade e incrementamos (+1) a variável correspondente
        if idade >= 18:
            maiores += 1
        else:
            menores += 1

# O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)# o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
print(f"Foram lidas o total de {idades_lidas} idades, com uma média de {soma_idades / idades_lidas} anos.")
print(f"{maiores} pessoas estão na maioridade enquanto {menores} pessoas são menores de idade")
    
