# https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=45

# Entrada de dados:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Processamento e Saída de dados:
if n1 > n2 and n1 > n3:
    print('{} é o maior número digitado'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior número digitado'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior número digitado'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor número digitado'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor número digitado'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor número digitado'.format(n3))
