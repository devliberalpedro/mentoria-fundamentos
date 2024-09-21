'''
Escreva um programa que lê um arquivo .txt contendo endereços IPs, da seguinte forma:

200.135.80.9
192.268.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O programa deve mostrar os IPs indicando os que são válidos e inválidos (um
endereço IP válido não pode ter uma de suas partes maior que 255).
'''

# Nome do arquivo que contém os endereços IP
nome_arquivo = "./Lista 5/ips.txt"

# Abre o arquivo em modo de leitura ('r')
with open(nome_arquivo, "r") as arquivo:
    # Lê todas as linhas do arquivo e armazena em uma lista
    ips = arquivo.readlines()

# Itera sobre cada IP na lista
for ip in ips:
    # Remove espaços em branco e caracteres de nova linha do IP
    ip = ip.strip()

    # Divide o IP em suas partes usando o ponto como delimitador. Armazena em uma nova lista
    partes_ip = ip.split(".")

    # Verifica se o IP tem 4 partes
    if len(partes_ip) == 4:
        # Variável para armazenar se o IP é válido ou inválido
        situacao = ""

        # Verifica se cada parte é um número entre 0 e 255
        for parte in partes_ip:
            if int(parte) < 0 or int(parte) > 255:
                situacao = "Inválido"
                break
            else:
                situacao = "Válido"
        
        print(f"{ip} - {situacao}")
