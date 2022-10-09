# https://www.youtube.com/watch?v=23UOVEetNPY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=37

# Entrada de dados:
frase = str(input('Digite uma frase: ')).strip().upper()

# Saída de dados:
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))
