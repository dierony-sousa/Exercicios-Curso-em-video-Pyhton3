# https://www.youtube.com/watch?v=ePwP4gU_waY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=54

from datetime import date
atual = date.today().year

# Entrada de dados:
nasc = int(input('Digite o ano de nascimento, com 4 dígitos: '))

# Processamento:
idade = atual - nasc

# Saída de dados:
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem 18 anos, ainda falta {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(nasc+18))
else:
    print('Você já deveria ter se alisatado há {} anos.'.format(idade-18))
    print('Seu alistamento foi em {}'.format(nasc+18))
