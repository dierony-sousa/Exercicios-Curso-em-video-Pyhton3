# https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=24

# Entrada de dados:
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

# Processamento de dados:
valAluguel = 60.00 * dias
valKmrodado = 0.15 * km
valTotal = valAluguel + valKmrodado

# Saída de dados:
print('O valor total a pagar é de R${}'.format(valTotal))
