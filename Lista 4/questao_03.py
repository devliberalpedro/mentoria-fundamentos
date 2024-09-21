'''
Desenvolva uma função que permita receber uma variável inteira X inúmeras vezes (deve parar quando o valor digitado for igual a zero). Como retorno da função,
para cada valor lido deverá ser imprimido a sequência de 1 até X (o número digitado), com um espaço entre cada número e seu sucessor.
'''

# Define uma função para gerar a sequência numérica
def imprimir(valor):
    """
    Gera uma sequência numérica onde cada número de 1 até (valor - 1) é repetido 
    o mesmo número de vezes, separado por espaços.

    Args:
        valor (int): O limite superior da sequência (exclusivo).

    Returns:
        str: A sequência numérica gerada.
    """

    sequencia = ""  # Inicializa uma string vazia para armazenar a sequência

    # Itera de 1 até (valor - 1)
    for i in range(1, valor):
        # Adiciona o número 'i' repetido 'i' vezes à sequência, separado por espaços
        sequencia += " ".join(str(i)) 

    # Retorna a sequência
    return sequencia 

# Loop principal que continua até que o usuário digite 0
while True:
    # Solicita ao usuário um valor inteiro
    valor = int(input("Informe um valor: "))

    # Verifica se o usuário deseja sair (digitou 0)
    if valor == 0:
        break  # Sai do loop se o valor for 0

    # Chama a função para gerar a sequência e imprime o resultado
    print(imprimir(valor))
