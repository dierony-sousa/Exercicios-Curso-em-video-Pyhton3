# https://www.youtube.com/watch?v=xM4AX3Lp2mo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=19

# Entrada de dados:
dinReal = float(input('Quanto dinheiro você tem na carteira? R$'))

# Processamento de dados:
dolar = dinReal / 3.27

# Saída de dados:
print('Com R${} Você pode comprar U$${:.2f}'.format(dinReal, dolar))
