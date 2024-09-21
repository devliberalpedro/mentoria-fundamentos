'''
Faça uma função que retorne o reverso de um número inteiro informado pelo usuário
'''

# Função para reverter o número 
def reverso(numero):
    # Usa o método de manipulação de strings join para inverter o valor
    numero_reverso = ''.join(reversed(str(numero)))

    # Retorna o valor
    return int(numero_reverso)

# Pede que o usuário insira o número
numero = int(input("Informe um númer com ao menos 2 dígitos: "))

# Chama a função dentro do print, logo, ela será executada e o print exibirá o retorno desta função
print(reverso(numero))