# https://www.youtube.com/watch?v=QDpwjBYRcVE

listaNum = []
for c in range(5):
    n = int(input('Digite um número: '))
    if c == 0 or n > listaNum[-1]:
        listaNum.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(listaNum):
            if n <= listaNum[pos]:
                listaNum.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados, em ordem crescente foram {listaNum}.')
