# https://www.youtube.com/watch?v=IL5iBWoKRIs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=70

from datetime import date

# Entrada e Processamento de dados:
ano = date.today().year
maiorID = 0
menorID = 0
for c in range(1, 8):
    aNasc = int(input('Em que ano a {}ª pessoas nasceu? '.format(c)))
    idade = ano - aNasc
    if idade < 18:
        menorID += 1
    else:
        maiorID += 1

# Saída de dados:
print('\n{} Pessoas são menores de idade.\n{} pessoas são maiores de idade.'.format(menorID, maiorID))
