# https://www.youtube.com/watch?v=4Ca6iRJo3M0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=86

print('CADASTRO DE PESSOAS')
maiorID = masc = fem = menorID = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo biológico [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maiorID += 1
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        fem += 1
        if idade < 20:
            menorID += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar cadastrando? [S/N]')).upper().strip()[0]
    print('-'*35)
    if sair == 'N':
        break
print(f'Foram cadastradas {maiorID} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {masc} homens.')
print(f'Foram cadastradas {fem} mulheres e {menorID} delas têm menos de 20 anos de idade.')
