# https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=38

# Entrada de dados:
nomeC = str(input('Digite o nome completo: ')).strip()

# Processamento:
nome = nomeC.split()

# Saída de dados:
print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
