# https://www.youtube.com/watch?v=9dlBZlkvvxY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=76

# Entrada de dados:
num = int(input('Digite um número para saber o seu FATORIAL:'))

# Processamento de dados:
cont = num
fat = 1
while cont > 0:
    fat *= cont
    cont -= 1

# Saída de dados:
print('Fatorial de {}! = {}.'.format(num, fat))
