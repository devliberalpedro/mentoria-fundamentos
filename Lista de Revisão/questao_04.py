'''
Construa um programa que leia uma string e verifique se a string está contida em um arquivo 
de texto, retornando o resultado da verificação.
'''

# Define o caminho completo do arquivo a ser pesquisado
meu_arquivo = "./Lista de Revisão/arquivo_04.txt"

# Solicita ao usuário a palavra a ser pesquisada
pesquisa = input("Pesquisar no texto: ")

# Abre o arquivo no modo leitura, especificando a codificação UTF-8 para lidar com caracteres especiais
with open(meu_arquivo, "r", encoding="UTF-8") as arquivo:
    # Itera sobre cada linha do arquivo
    for linha in arquivo:
        # Verifica se a palavra pesquisada (em minúsculo) está na linha (em minúsculo)
        if pesquisa.lower() in linha.lower():
            retorno = True
            break  # Para a busca assim que a palavra é encontrada
        else:
            retorno = False

# Imprime o resultado da pesquisa
if retorno:
    print(f"A palavra foi encontrada no arquivo!")
else:
    print(f"A palavra não foi encontrada no arquivo!")