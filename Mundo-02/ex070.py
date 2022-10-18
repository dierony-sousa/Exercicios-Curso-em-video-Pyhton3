# https://www.youtube.com/watch?v=hS8QdW-1HTo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=88&t=1s

total = caros = barato = cont = 0
nomebarato = ''
print('--REGISTRADOR DE PRODUTOS--')
while True:
    nome = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: R$'))
    total += preco
    if preco > 1000:
        caros += 1
    cont += 1
    if cont == 1:
        barato = preco
        nomebarato = nome
    if preco < barato:
        barato = preco
        nomebarato = nome
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar registrando os produtos? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
print('-'*10, 'FINAL DA COMPRA', '-'*10)
print(f'VALOR TOTAL da compra: R${total:.2f}')
print(f'Custou MAIS DE R$1.000: {caros} produtos.')
print(f'O produto {nomebarato} foi o mais barato, custou R${barato:.2f}.')
