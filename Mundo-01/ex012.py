# https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=21

# Entrada de dados:
preco = float(input('Qual é o preço do produto? R$ '))

# Processamento de dados:
precoF = preco - (preco * (5/100))

# Saída de dados:
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, precoF))
