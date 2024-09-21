'''
1. Questão 01

Um programa de vida saudável quer dar pontos para atividades físicas, os quais poderão ser trocados por dinheiro. O sistema funciona assim:

- até 10 horas de atividades no mês: ganha 2 pontos por hora;
- de 11 até 20 horas de atividades por mês: ganha 5 pontos por hora
- acima de 20 horas de atividades por mês: ganha 10 pontos por hora.

Faça um programa que leia quantas horas de atividades uma pessoa teve por mês, calcule e mostre quantos pontos ela obteve.
'''

# Realizamos o input convertendo para o tipo inteiro, para facilitar a lógica do código. Lembrem-se que o input, por padrão, sem conversão, receberá uma string!
horas_atividades = int(input("Quantidade de horas de atividades: "))

# Precisamos analizar apenas duas condições, uma vez que, se ambas não forem atendidas, obrigatoriamente entramos no terceiro intervalor de pontuação
# Primeiro verificamos se o valor é menor ou igual a 10, em seguida verificamos se está no intervalo entre 11 e 20 horas. Caso não esteja em ambas, entra acima de 20 horas
if horas_atividades <= 10:
    # O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
    # o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
    print(f"Você acumulou {horas_atividades * 2} pontos no mês")
elif horas_atividades >= 11 and horas_atividades <= 20:
    print(f"Você acumulou {horas_atividades * 5} pontos no mês")
else:
    print(f"Você acumulou {horas_atividades * 10} pontos no mês")

'''
## Observações:

Para um programa mais robusco, caso deseje, podemos verificar se o número inserido é
zero ou negativo e informar uma quantidade inválida de horas de atividade. Também podemos calcular o tempo máximo de horas em um mês (720 horas para meses com 30 dias)
'''