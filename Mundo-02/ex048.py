# https://www.youtube.com/watch?v=iHjsUxNA-wo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=64

# Processamento e Saída de dados:
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma entre os números ímpares, múltimplos de 3, no intervalo entre 1 até 500 é\033[32m {}\033[m.'.format(soma))
