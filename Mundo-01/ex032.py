# https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=44

from datetime import date

# Entrada de dados:
ano = int(input('Digite qual ano você quer saber se é bissexto,\nou digite 0 para saber o ano atual: '))

# Processamento e Saída de dados:
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
