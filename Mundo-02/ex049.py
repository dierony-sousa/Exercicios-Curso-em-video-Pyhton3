# https://www.youtube.com/watch?v=QtElJDa9ICM&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=65

# Entrada de dados:
num = int(input('Digite um número: '))

# Processamento e Saída de dados:
print('-'*12)
print('Tabuada de {}'.format(num))
print('-'*12)
for c in range(1, 11):
    x = num * c
    print('{} X {} = {}'.format(num, c, x))
print("-"*12)
