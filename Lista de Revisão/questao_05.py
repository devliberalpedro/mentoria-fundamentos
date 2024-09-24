'''
As professoras Carol e Natasha querem saber os alunos que mais conversam nas aulas. Crie 
um aplicativo que leia o nome e o sobrenome de um aluno sempre que ele conversar na aula 
e o armazene em um arquivo de texto (.txt). O programa deverá parar de aceitar novos nomes 
quando o valor digitado for "sair".

Após todos os nomes serem inseridos, leia o arquivo e imprima na tela os nomes que aparecem 
mais de uma vez!
'''

meu_arquivo = "./Lista de Revisão/arquivo_05.txt"

# Lista para armazenar os nomes dos alunos que conversaram mais de uma vez
conversadores = []

# Abre o arquivo no modo de escrita, criando-o se não existir
with open(meu_arquivo, "w", encoding="UTF-8") as arquivo:
    while True:
        nome = input("Digite o nome completo do aluno (ou 'sair' para encerrar): ")

        # Converte o nome para minúsculas para facilitar a comparação
        if nome.lower() == "sair":
            break

        # Escreve o nome no arquivo, adicionando uma nova linha
        arquivo.write(nome + "\n")

# Abre o arquivo no modo de leitura
with open(meu_arquivo, "r", encoding="UTF-8") as arquivo:
    # Lê todas as linhas do arquivo e as armazena em uma lista
    nomes = arquivo.read().splitlines()

    # Itera sobre cada nome na lista
    for nome in nomes:
        # Verifica se o nome aparece mais de uma vez na lista
        if nomes.count(nome) > 1:
            # Verifica se o nome ainda não foi adicionado à lista de conversadores
            if nome not in conversadores:
                conversadores.append(nome)

# Imprime os nomes dos alunos que conversaram mais de uma vez
for amostradinho in conversadores:
    print(f"{amostradinho.capitalize()} é um/uma amostradinho/amostradinha e conversou demais!")