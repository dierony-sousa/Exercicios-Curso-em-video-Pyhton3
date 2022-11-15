# https://www.youtube.com/watch?v=EGmlFdwD4C4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=107

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('--'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
