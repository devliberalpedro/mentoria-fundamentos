'''
Questão 03

Desenvolva um programa que leia a área em m² de um terreno retangular. Ao final, o programa deverá mostrar a classificação deste terreno, de acordo com a lista abaixo:

- Abaixo de 100m²: TERRENO POPULAR
- Entre 100m² e 500m²: TERRENO MASTER
- Acima de 500m²: TERRENO VIP

Obs: Cálculo da área de um retângulo: Área = Base X Altura
'''

# Realizamos a conversão do input para o tipo float, pois o padrão do input é receber uma string.
base = float(input("Qual a base do terreno: "))
altura = float(input("Qual a altura do terreno: "))

# Realizamos o cálculo da área deste retângulo
area = base * altura

# Usamos o else nestas condicionais para garantir que, se o usuário inserir o valor zero ou valor negativo, não apresentará
# um terreno de área nula ou negativa, otimizando nosso código
if area > 0 and area < 100:
    print("Terreno popular")
elif area >= 100 and area <= 500:
    print("Terreno master")
elif area > 500:
    print("Terreno VIP")
else:
    print("Tamanho inválido!")