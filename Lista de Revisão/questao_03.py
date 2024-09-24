'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
formais: taxa_imposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
custo,  que  é  o  custo  de  um  item  antes  do  imposto. A  função  “altera”  o  valor  de  custo  para  
incluir o imposto sobre vendas. Imprima o custo inicial, o imposto aplicado e o novo valor.
'''

def somaImposto(taxa_imposto, custo):
    """
    Calcula o valor total de um produto após a aplicação de um imposto.

    Args:
        taxa_imposto: Taxa de imposto sobre vendas em porcentagem.
        custo: Custo do produto antes do imposto.

    Returns:
        None (Imprime os valores na tela).
    """
    print(f"Custo inicial do produto: R${custo}")
    print(f"Imposto aplicado: {taxa_imposto}%")

    # Cálculo do valor do imposto e adição ao custo original
    valor_imposto = (custo * taxa_imposto) / 100
    novo_custo = custo + valor_imposto
    print(f"Novo custo do produto: R${novo_custo}")

# Solicita ao usuário o valor do produto e a taxa de imposto
custo = float(input("Valor do produto: "))
taxa_imposto = float(input("Valor do imposto (em percentual): "))

# Chama a função para calcular e imprimir o novo valor
somaImposto(taxa_imposto, custo)