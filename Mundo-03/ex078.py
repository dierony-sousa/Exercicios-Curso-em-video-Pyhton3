# https://www.youtube.com/watch?v=q8Z1cRdJnfk

num = []
maior = menor = 0
for pos in range(5):
    num.append(int(input(f'Informe um número para a posição {pos}: ')))
    if pos == 0:
        maior = menor = num[pos]
    else:
        if num[pos] > maior:
            maior = num[pos]
        elif num[pos] < menor:
            menor = num[pos]
print('-'*40)
print(f'Você informou os valores {num}.')
print(f'\nO MAIOR número digitado foi {maior} na posição ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO MENOR número digitado foi {menor} na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end=' ')
