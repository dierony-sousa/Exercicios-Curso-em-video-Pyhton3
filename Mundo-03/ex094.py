# https://youtu.be/ETnExBCFeps

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite uma opção válida! ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite uma opção válida! ')
    if resp == 'N':
        break
print('--'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'Lista das pessoas com idade acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
