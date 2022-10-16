# https://www.youtube.com/watch?v=vu5ehetQGe8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=78

# Entrada de dados:
primeiro = (int(input('Primeiro termo: ')))
razao = (int(input('Digite a razão: ')))

# Processamento e Saída de dados:
termo = primeiro
cont = 0
while cont < 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM!')
