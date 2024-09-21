'''
Questão 04

Uma loja de roupa está em promoção: Acima de 2 peças de roupas compradas e fazendo o pagamento à vista, o cliente tem 20% de desconto no valor total.

Faça um algorítmo que receba:

- A quantidade de peças compradas
- O valor total da compra
- O código referente a condição de pagamento

1. À vista
2. Crédito
3. Crédito parcelado

Por fim, o algorítmo deverá apresentar uma mensagem informando se o desconto foi aplicado, e em caso positivo, o novo valor da compra
'''

# Realizamos os inputs convertendo para os respectivos tipos. Lembrem-se, o input recebe uma string por padrão.
quantidade = int(input("Quantas peças foram compradas: "))
valor = float(input("Valor total da compra: "))

print("Forma de pagamento:")
print("  1. À vista")
print("  2. Crédito")
print("  3. Crédito parcelado")
# Convertemos a entrada do usuário para facilitar a verificação da condicional
forma = int(input("Forma de pagamento: "))

# A única forma do desconto ser aplicado é caso a forma de pagamento seja à vista (valor 1) e a quantidade de peças
# for igual ou maior que 2.
if forma == 1 and quantidade >= 2:
    print("Desconto aplicado!")
    # O uso do print formatado (o tal do 'f' antes das aspas duplas, ajuda a manter o código legível)
    # o entendimento dele é simples: irá escrever a saída de sua string e, quando desejar imprimir o valor de uma variável nela, basta colocar entre chaves. Exemplo: {variável}
    print(f"Valor da compra sem desconto: {valor}")
    print(f"Valor da compra com desconto: {valor * 0.8}")
else:
    print("Desconto não aplicado!")
    print(f"Valor da compra: {valor}")