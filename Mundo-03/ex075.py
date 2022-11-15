# https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=94

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for p in num:
    if p % 2 == 0:
        print(f'{p} ', end='')
