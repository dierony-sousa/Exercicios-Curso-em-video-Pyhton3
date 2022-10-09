# https://www.youtube.com/watch?v=_QfISzy0IKs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=16

# Entrada de dados:
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

# Processamento de dados:
media = (nota1 + nota2) / 2

# Saída de dados:
print('A média entre {} e {} é igual a {:.1f}'.format(nota1, nota2, media))
