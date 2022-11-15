# https://www.youtube.com/watch?v=HipQYUk4koA&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=112

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {"nome"}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('--'*17)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
