# https://www.youtube.com/watch?v=QhS829x6up4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=108

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('--'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()
print('--'*30)
print(f'A SOMA dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A SOMA dos valores da 3ª coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O Maior valor da 2ª linha é {maior}.')
