# https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=29

from random import choice

# Entrada de dados:
alu1 = input('Nome do 1º aluno: ')
alu2 = input('Nome do 2º aluno: ')
alu3 = input('Nome do 3º aluno: ')
alu4 = input('Nome do 4º aluno: ')

# Processamento de dados:
lista = [alu1, alu2, alu3, alu4]

# Saída de dados:
print('O aluno sorteado foi {}'.format(choice(lista)))
