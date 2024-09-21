'''
Por conta da pandemia, o CEF (Curso Estudante Feliz) adotou o Google Classroom como ferramenta para auxiliar o ensino remoto. Para acessá-lo, os estudantes precisam logar com e-mail institucional e senha.

A senha inicial, enviada pela Agenda Digital, é gerada automaticamente a partir da data de nascimento do aluno, do seguinte modo:

mm + ‘$’ + dd(invertido) + ‘#’ + dd + ‘!’ + mm(invertido) + ‘*’ + aaaa

Escreva um programa que leia o dia, mês e ano de nascimento de um estudante e informe a senha de acordo com a formatação acima.
'''

# Define a função que gera a senha
def gerar_senha(dia, mes, ano):
    """
    Gera uma senha a partir da data de nascimento.

    Args:
        dia (str): Dia de nascimento (dois dígitos).
        mes (str): Mês de nascimento (dois dígitos).
        ano (str): Ano de nascimento (quatro dígitos).

    Returns:
        str: A senha gerada.
    """
    # Constrói a senha final concatenando os componentes da data em uma ordem específica
    # com caracteres especiais como separadores.
    return "Sua senha é: " + mes + "$" + ''.join(reversed(dia)) + "#" + dia + "!" + ''.join(reversed(mes)) + "*" + ano

# Inicializa as variáveis para armazenar dia, mês e ano
dia = mes = ano = ""

# Loop para obter o dia de nascimento com validação
while len(dia) != 2:
    dia = input("Insira o dia de seu nascimento (dd): ")
    if len(dia) != 2:
        print(">> O dia precisa ter dois dígitos! <<")

# Loop para obter o mês de nascimento com validação
while len(mes) != 2:
    mes = input("Insira o mês de seu nascimento (mm): ")
    if len(mes) != 2:
        print(">> O mês precisa ter dois dígitos! <<")

# Loop para obter o ano de nascimento com validação
while len(ano) != 4:
    ano = input("Informe o ano de seu nascimento (yyyy): ")
    if len(ano) != 4:
        print(">> O ano precisa ter quatro dígitos! << ")

# Chama a função para gerar a senha e imprime o resultado
print(gerar_senha(dia, mes, ano))