# https://www.youtube.com/watch?v=Kjpb_IAOKRQ&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=71

# Entrada e Processamento de dados:
maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = (float(input('Digite o peso da {}ª pessoa: '.format(c))))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        elif peso < menorpeso:
            menorpeso = peso

# Saída de dados:
print('O maior peso lido foi de {}kg'.format(maiorpeso))
print('O menor peso lido foi de {}kg'.format(menorpeso))
