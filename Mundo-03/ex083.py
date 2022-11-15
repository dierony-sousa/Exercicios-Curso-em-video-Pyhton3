# https://www.youtube.com/watch?v=dvhP41Z7TLk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=103

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida')
