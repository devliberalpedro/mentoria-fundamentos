'''
A funenária Sua Hora Chegou possui vários caixões. O algorítmo deverá cadastrar o código dos caixões até o usuário digitar -1 (quando digitar -1 ele encerra) e
sair do cadastro. Por fim, o algorítmo mostrará o número de caixões cadastrados. Utilize o while.
'''

# Armazenará o total de caixões.
qtd_caixoes = 0

# Usamos o while True quando não sabemos quantas repetições teremos
# Neste caso, nossa condição de parar as repetições é o usuário inserir o valor -1
# Por conta disto, precisamos verificar o valor inseriro logo após o input, para evitar que o valor -1 seja calculado em alguma variável
while True:
    # Realizamos o input convertendo para o tipo inteiro, para facilitar a lógica do código. Lembrem-se que o input, por padrão, sem conversão, receberá uma string!
    codigo = int(input("Informe o código do caixão: "))

    # Validamos se o valor inserido equivale à condição de saída do loop
    if codigo == -1:
        # O break é o comando que encerra, imediatamente, o loop que está em execução.
        break

    # Caso o valor não seja equivalente à condição de saída, incrementamos a quantidade de caixões (+1)
    qtd_caixoes += 1

# O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
# o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
print(f"Foi/Foram cadastrado(s) um total de {qtd_caixoes} caixão/caixões no sistema")