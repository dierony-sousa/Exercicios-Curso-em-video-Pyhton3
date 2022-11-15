# https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=106

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('--'*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digigatos foram: {num[1]}')
