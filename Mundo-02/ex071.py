# https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=89

print('-'*17, 'CAIXA ELETRÔNICO', '-'*17)
print('Céduas disponíveis R$: 50,00 | 20,00 | 10,00 | 1,00')
valor = int(input('Qual valor deseja sacar? R$ '))
cinquenta = vinte = dez = um = 0
while valor >= 50:
    valor -= 50
    cinquenta += 1
while valor >= 20:
    valor -= 20
    vinte += 1
while valor >= 10:
    valor -= 10
    dez += 1
while valor >= 1:
    valor -= 1
    um += 1
print('-'*17, 'RETIRE as cédulas do caixa!', '-'*17)
if cinquenta >= 1:
    print(f'{cinquenta} notas de R$ 50,00')
if vinte >= 1:
    print(f'{vinte} notas de R$ 20,00')
if dez >= 1:
    print(f'{dez} notas de R$ 10,00')
if um >= 1:
    print(f'{um} notas de R$ 1,00')
print('Volte sempre!')
