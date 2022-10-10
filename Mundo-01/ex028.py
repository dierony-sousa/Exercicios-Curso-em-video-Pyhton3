# https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=40

from random import randint

# Processamento de dados:
numpc = randint(0, 5)

print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*18)

# Entrada de dados:
num = int(input('Qual número eu pensei? '))

# Saída de dados:
if numpc == num:
    print('Eu pensei no nº {}, Parabéns, você acertou!'.format(numpc))
else:
    print('Eu penseu no nº {}, Errou! Tente de novo!'.format(numpc))
