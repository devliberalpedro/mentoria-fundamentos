'''
Maria está organizando uma lista de convidados para uma festa. No entanto, ela
escreveu os nomes dos convidados várias vezes enquanto os anotava, resultando
em muitas duplicatas. Ela decidiu escrever todos os nomes em um arquivo de
texto (.txt) para facilitar a análise. Elabore um programa que, baseado nas
entradas de nomes que Maria irá escrever em um arquivo de texto (.txt), mostre
na tela quais nomes apareceram mais de uma vez (nomes repetidos). Considere
letras maiúsculas e minúsculas, exemplo: Carol e carol, seriam nomes repetidos.
O programa encerra quando for digitado o nome SAIR, utilize o while.

'''

# Define o caminho completo do arquivo a ser criado
meu_arquivo = "./Prova 2024-1/arquivo_02.txt"

# Lista para armazenar os nomes repetidos
repetidos = []

# Abre o arquivo no modo de escrita, criando-o se não existir, e codificando em UTF-8
with open(meu_arquivo, "w", encoding="UTF-8") as arquivo:
    # Loop para coletar os nomes dos convidados
    while True:
        nome = input("Digite o nome do convidado/a (ou 'sair' para encerrar): ")

        # Condição para encerrar o loop se o usuário digitar 'sair'
        if nome.upper() == "SAIR":
            break

        # Escreve o nome no arquivo, capitalizando a primeira letra e adicionando uma nova linha
        arquivo.write(nome.capitalize() + "\n")

# Abre o arquivo no modo de leitura, codificando em UTF-8
with open(meu_arquivo, "r", encoding="UTF-8") as arquivo:
    # Lê todas as linhas do arquivo e as coloca em uma lista
    nomes_repetidos = arquivo.read().splitlines()

    # Itera sobre cada nome na lista de nomes repetidos
    for nome in nomes_repetidos:
        # Verifica se o nome aparece mais de uma vez na lista
        if nomes_repetidos.count(nome) > 1:
            # Verifica se o nome já foi adicionado à lista de repetidos
            if nome not in repetidos:
                # Adiciona o nome à lista de repetidos
                repetidos.append(nome)

# Imprime os nomes repetidos, capitalizando a primeira letra
print("Nomes repetidos:")
for nome in repetidos:
    print(f"- {nome.capitalize()}")