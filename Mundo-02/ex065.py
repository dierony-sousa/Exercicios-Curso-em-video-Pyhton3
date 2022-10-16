# https://www.youtube.com/watch?v=QNPuPlPM--0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=81

# Entrada e Processamento de dados:
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
media = soma / quant

# Saída de dados:
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
