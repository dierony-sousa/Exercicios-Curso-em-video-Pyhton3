# https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=43

# Entrada de dados:
km = float(input('Qual a distância da viagem em km? '))

# Processamento e Saída de dados:
if km <= 200:
    print('O preço da passagem é R$ {:.2f}'.format(km * 0.50))
else:
    print('O preço da passagem é R$ {:.2f}'.format(km * 0.45))
