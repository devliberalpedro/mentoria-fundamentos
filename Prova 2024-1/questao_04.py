'''
A banda "Raça Negra" possui um sistema de reprodução de músicas em seu estúdio,
com seis botões numerados de 0 a 5. Eles têm uma lista de suas 7 melhores músicas.
Para tocar uma música, é necessário pressionar dois botões no sistema. Os números
desses dois botões são somados, e a música correspondente ao número da soma é
reproduzida, conforme a lista abaixo. Por exemplo, se os botões pressionados forem
1 e 4, será reproduzida a música 5 – "Ciúme de Você". Escreva um programa que,
dados os dois botões pressionados, determine qual música será reproduzida.
0 - "Cheia de manias"
1 - "Me leva junto com você"
2 - "É tarde demais"
3 - "Quando te encontrei"
4 - "Deus me livre"
5 - "Ciúme de Você"
6 - "Cigana"
Cada botão está numerado de 0 a 5. Caso a soma esteja fora do intervalo, notificar.
'''

# Lista de músicas disponíveis para reprodução
musicas = ["Cheia de manias", "Me leva junto com você", "É tarde demais", "Quando te encontrei", "Deus me livre", "Ciúme de Você", "Cigana"]

# Imprime o menu com as opções de músicas
print("Menu:")
for idx, musica in enumerate(musicas):
    print(f"{idx} - {musica}")

# Loop para garantir que o primeiro botão seja pressionado corretamente
while True:
    # Solicita ao usuário que pressione o primeiro botão e converte a entrada para um número inteiro
    botao_1 = int(input("Pressione o primeiro botão (0 - 5): "))

    # Verifica se o valor do botão está dentro do intervalo válido
    if 0 <= botao_1 <= 5:
        # Se o valor for válido, sai do loop
        break
    else:
        # Se o valor for inválido, informa o usuário e volta ao início do loop
        print(">> Botão inválido!")

# Loop para garantir que o segundo botão seja pressionado corretamente
# (mesmo funcionamento do loop anterior)
while True:
    botao_2 = int(input("Pressione o segundo botão (0 - 5): "))

    if 0 <= botao_2 <= 5:
        break
    
    print(">> Botão inválido!")

# Calcula a soma dos valores dos botões
soma = botao_1 + botao_2

# Verifica se a soma dos botões corresponde a um índice válido na lista de músicas
if soma > 6:
    # Se a soma for maior que 6, a música não existe
    print(">> Música não encontrada")
else:
    # Se a soma for válida, reproduz a música correspondente
    print(f"Reproduzindo a música: {musicas[soma]}")