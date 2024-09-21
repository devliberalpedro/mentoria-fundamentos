'''
Faça um programa que tenha duas funções. A primeira função irá receber como
parâmetro o nome de um arquivo, e o abrirá em formato de escrita. Nesse arquivo
deve ser armazenado o nome e sobrenome de 6 pessoas, 1 pessoa por linha.
A segunda função receberá o nome do arquivo criado na função anterior,
apresentará um nome e sobrenome por vez e perguntará se o usuário deseja
alterá-lo. Se o usuário digitar ‘Sim’, deverá alterar a linha com novas informações,
senão, a linha permanece com o mesmo nome e sobrenome. As modificações
devem ser salvas no mesmo arquivo.
'''

def armazenar_nomes(nome_arquivo):
    # Armazena nomes e sobrenomes em um arquivo.
    with open(nome_arquivo, 'w') as arquivo:
        for idx in range(6):
            nome_completo = input("Digite o nome e sobrenome (separados por espaço): ")
            arquivo.write(nome_completo + '\n')

def alterar_nomes(nome_arquivo):
    # Permite ao usuário alterar nomes e sobrenomes em um arquivo.
    with open(nome_arquivo, 'r+') as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)  # Volta ao início do arquivo para sobrescrever
        arquivo.truncate()  # Limpa o conteúdo do arquivo

    for linha in linhas:
        nome_completo = linha.strip()
        print(f"Nome atual: {nome_completo}")
        alterar = input("Deseja alterar? (Sim/Não): ").lower()
        if alterar == 'sim':
            novo_nome = input("Digite o novo nome e sobrenome: ")
            arquivo.write(novo_nome + '\n')
        else:
            arquivo.write(nome_completo + '\n')

# Execução do programa
nome_arquivo = 'nomes.txt'
armazenar_nomes(nome_arquivo)
alterar_nomes(nome_arquivo)
