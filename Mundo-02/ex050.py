# https://www.youtube.com/watch?v=rJaBLOW57Jg&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=65

# Entrada e Processamento de dados:
soma = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num

# Saída de dados:
print('A soma dos números PARES que você digitou é \033[32m{}.\033[m'.format(soma))
