# https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=30

from random import shuffle

# Entrada de dados:
alu1 = str(input('Nome do 1º aluno: '))
alu2 = str(input('Nome do 2º aluno: '))
alu3 = str(input('Nome do 3º aluno: '))
alu4 = str(input('Nome do 4º aluno: '))

# Processamento de dados:
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)

# Saída de dados:
print('A ordem de apresentação será:{}'.format(lista))

