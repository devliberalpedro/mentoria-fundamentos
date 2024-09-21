'''
Faça uma função que receba uma lista de números e dois valores (limite inferior e limite superior). A função deverá retornar uma lista cujo os elementos
são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

No programa principal, informe 10 números inteiros, armazenando-os numa lista. Informe também o limite inferior e o limite superior.

Teste a função implementada e exiba o resultado.
'''

# Define uma função para criar uma nova lista com valores dentro de um intervalo
def nova_lista(lista, inferior, superior):
    """
    Cria uma nova lista contendo apenas os valores da lista original que estão
    dentro do intervalo especificado.

    Args:
        lista: A lista original de números.
        inferior: O limite inferior do intervalo (inclusive).
        superior: O limite superior do intervalo (inclusive).

    Returns:
        Uma nova lista contendo os valores filtrados.
    """

    nova_lista = []  # Inicializa uma lista vazia para armazenar os valores filtrados

    # Itera sobre cada valor na lista original
    for valor in lista:
        # Verifica se o valor está dentro do intervalo
        if inferior <= valor <= superior:
            nova_lista.append(valor)  # Adiciona o valor à nova lista se estiver dentro do intervalo

    return nova_lista  # Retorna a nova lista filtrada

# Cria uma lista vazia para armazenar os números inseridos pelo usuário
lista = []

# Loop para solicitar 10 números ao usuário
for idx in range(10):
    numero = int(input(f"Insira o {idx + 1}º número: "))
    lista.append(numero)  # Adiciona o número à lista

# Solicita ao usuário o limite inferior do intervalo
inferior = int(input("Insira o limite inferior: "))

# Solicita ao usuário o limite superior do intervalo
superior = int(input("Insira o limite superior: "))

# Chama a função para filtrar a lista e imprime o resultado
print(nova_lista(lista, inferior, superior))