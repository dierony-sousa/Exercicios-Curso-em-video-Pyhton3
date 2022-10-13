# https://www.youtube.com/watch?v=ZiC5NgSGJXU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=56

from datetime import date
ano = date.today().year

# Entrada de dados:
nasc = int(input('Qual o ano de nascimento do atleta? '))

# Processamento de dados:
idade = ano - nasc

# Saída de dados:
if idade <= 9:
    print('O atleta tem {} anos, categoria MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, categoria INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos, categoria JÚNIOR'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos, categoria SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos, categoria MASTER'.format(idade))
