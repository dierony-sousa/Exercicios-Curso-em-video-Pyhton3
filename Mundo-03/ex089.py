# https://www.youtube.com/watch?v=7xrCJnniqMw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=109&t=2s

from time import sleep
ficha = []
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('--'*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--'*30)
    opc = int(input('Digite o nº da lista para ver as notas do aluno: [999 para ENCERRAR]:'))
    if opc == 999:
        print('Finalizando...')
        sleep(1)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte Sempre!')
