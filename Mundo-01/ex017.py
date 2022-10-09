# https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=27

from math import hypot

# Entrada de dados:
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjacente: '))

# Saída de dados:
print('A hipotenusa vai medir {:.2f}'.format(hypot(b, c)))
