'''
Uma empresa irá realizar uma queima de estoque com os produtos que tiverem poucas unidades disponíveis. Os descontos aplicados seguem os seguintes critérios:

- 40% de desconto: até 2 unidades;
- 30% de desconto: entre 3 e 5 unidades;
- 20% de desconto: entre 6 e 9 unidades;
- 10% de desconto: 10 unidades ou mais

Faça um programa que receba o código do produto (número inteiro positivo), o valor unitário e o total em estoque. Para cada produto informado o sistema deverá apresentar qual desconto foi concedido e o novo valor unitário.

O sistema irá finalizar quando forem digitados 6 códigos de produto.
'''

# Crio as variáveis para armazenar o valor do desconto, o código, o estoque e o valor, iniciando com zero
desconto = codigo = estoque = valor = 0

# Toda a lógica estará dentro deste for
# Ele irá repetir 6 vezes e, a cada interação, irá receber um código, um valor e a quantidade em estoque
for idx in range(6):
    # Coloquei o input do código dentro de um while para garantir que ele será positivo e maior que zero
    # Enquanto isto não ocorrer, ficará pedindo para inserir o código
    while codigo <= 0:
        codigo = int(input(f"Insira o código do {idx + 1} produto: "))
    
    # Mesma lógica do código
    while valor <= 0:
        valor = float(input(f"Insira o valor unitário do {idx + 1} produto: "))
    
    # Mesma lógica do código e do valor
    while estoque <= 0:
        estoque = int(input(f"Insira o estoque da {idx +1} peça: "))

    # Após receber os valores acima, precisamos verificar em qual porcentagem de desconto esta peça se enquadra
    # Fazemos diversos if / elif / else para verificar todos os casos
    # Também aproveitamos para calcular o novo valor unitário com o desconto aplicado
    if 1 <= estoque >= 2:
        desconto = 40
        valor = valor * 0.6
    elif 3 <= estoque <= 5:     # isto é o mesmo que elif estoque >= 3 and estoque <= 5:
        desconto = 30
        valor = valor * 0.7
    elif 6 <= estoque <= 9:     # isto é o mesmo que elif estoque >= 6 and estoque <= 9:
        desconto = 20
        valor = valor * 0.8
    # Não uso elfi por já garanti, no input, que não terei valor igual ou menor à zero,
    # logo, todas as possibilidades foram atendidas nas condicionais
    else:
        desconto = 10
        valor = valor * 0.9

    # Como já sabemos o desconto aplicado e o novo valor, usamos nosso print formatado para mostrar tudo em tela
    print(f"A peça de código {codigo} teve concedido um desconto de {desconto}, ficando com o novo valor unitário de {valor}")