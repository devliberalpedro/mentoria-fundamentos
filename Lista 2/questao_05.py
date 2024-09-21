'''
Desenvolva um programa utilizando o for que faça a tabuada de um número inteiro que será digitado pelo usuário.
Mas a tabuada não deve, necessariamente, iniciar em 1 e terminar em 10, o valor inicial deve ser informado pelo usuário.

Exemplo (mostrar a tabuada de 5):
- Começar por 4
- terminar em 7

Saída de dados:
- 5x4 = 20
- 5x5 = 25
- 5x6 = 30
- 5x7 = 35
'''

# Solicita ao usuário o número para o qual deseja gerar a tabuada
tabuada = int(input("Informe a tabuada: "))

# Solicita o início do intervalo de multiplicadores
inicial = int(input("Informe o número multiplicador inicial: "))

# Solicita o fim do intervalo de multiplicadores
final = int(input("Informe o número multiplicador final: "))

# Itera sobre o intervalo de multiplicadores, incluindo o valor final
# É necessário adicionar 1 ao valor final para que ele entre na tabuada
for idx in range(inicial, (final + 1)):
    # Calcula o produto e imprime a linha da tabuada usando f-string
    print(f"{tabuada} x {idx} = {tabuada * idx}")
