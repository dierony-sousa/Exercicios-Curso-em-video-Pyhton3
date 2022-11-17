# https://www.youtube.com/watch?v=Vsqemzdrj78&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=114

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento(YYYY): '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho [0 - Não possui]: '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('--'*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
