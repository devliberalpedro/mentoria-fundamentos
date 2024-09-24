'''
Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, o mês e o ano 
para 3 variáveis inteiras. Antes disso, verifique se as barras estão no lugar certo e se “DD”, 
“MM” e “AAAA” são numéricos.

Caso os critérios acima sejam verdadeiros, imprima que a data é válida, senão, imprima que a data é inválida!
'''

data = input("Informe a data (dd/mm/aaaa): ")

# Verifica se a data tem o formato correto (10 caracteres e 2 barras)
if len(data) == 10 and data.count("/") == 2:
    # Verifica se as barras estão nas posições corretas (2ª e 5ª posições)
    if data[2] == "/" and data[5] == "/":
        # Separa a string em dia, mês e ano
        dia, mes, ano = data.split("/")

        # Converte as strings para números inteiros
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        # Verifica se os valores estão dentro dos limites válidos
        if (1 <= dia <= 31) and (1 <= mes <= 12) and ano > 0:
            print("Data válida!")
        else:
            print("Data inválida")
    else:
        print("Data inválida: as barras estão em posições incorretas.")
else:
    print("Data inválida: formato incorreto.")