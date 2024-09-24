'''
Escreva  um  programa  que  leia  um  arquivo  com  um  conjunto  de  nomes  (1  por  linha).  O  
programa deve ordenar os nomes e gerar um novo arquivo com os nomes ordenados.
'''

meu_arquivo = "./Lista de Revisão/arquivo_05.txt"  # Define o caminho do arquivo a ser lido e escrito

# Abre o arquivo no modo leitura e escrita (r+). O encoding "UTF-8" garante a compatibilidade com diferentes caracteres.
with open(meu_arquivo, "r+", encoding="UTF-8") as arquivo:
    # Lê todas as linhas do arquivo e armazena em uma lista
    conteudo_arquivo = arquivo.readlines()

    # Ordena a lista de nomes em ordem alfabética
    conteudo_arquivo.sort()

    # Move o cursor para o início do arquivo
    arquivo.seek(0)

    # Trunca o arquivo, removendo todo o conteúdo existente (não recomendado em modo r+)
    arquivo.truncate()

    # Escreve cada linha da lista ordenada de volta no arquivo, removendo espaços em branco no final
    for linha in conteudo_arquivo:
        linha = linha.strip()  # Remove espaços em branco no início e no final da linha
        arquivo.write(linha + '\n')  # Escreve a linha no arquivo, adicionando uma nova linha ao final