'''
Questão 02

Precisa-se desenvolver um sistema para verificar se um aluno foi aprovado na disciplina. Pede-se que o professor insira as duas notas do aluno e a sua frequência em porcentagem.

Primeiro, verifica-se se o aluno teve 75% de frequência, caso seja verdadeiro, verifica-se se a média do aluno é maior ou igual a 7, mostrando a mensagem "Aprovado por média". Se não, mostra-se a mensagem "Reprovado por média"

Mas, se a frequência for abaixo de 75%, mostra a mensagem "Reprovado por falta"
'''

# As notas deverão ser convertidas para ponto flutuante no input. Lembrem-se que o input, por padrão, sem conversão, receberá uma string.
nota1 = float(input("Insira a 1ª nota: "))
nota2 = float(input("Insira a 2ª nota: "))

# A frequência deverá ser convertida para um inteiro no input. Lembrem-se que o input, por padrão, sem conversão, receberá uma string!
frequencia = int(input("Insira a frequência do aluno (em porcentagem): "))

# Primeiro verificamos a frequência do aluno pois, caso seja inferior ao mínimo solicitado, não precisamos executar o cálculo da média e entramos no else, 
# imprimindo que o aluno foi reprovado por falta
if frequencia >= 75:
    # Calculamos a média e verificamos em qual condição ela se e enquadra: Se maior ou igual a sete, imprime que foi aprovado, caso inferior, imprime reprovado
    media = (nota1 + nota2) / 2

    if media >= 7:
        # O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
        # o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves.
        # Exemplo: {variável}
        print(f"Aprovado por média. Nota: {media}")
    else:
        print(f"Reprovado por média. Nota: {media}")
else:
    print("Reprovado por falta")