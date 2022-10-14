# https://www.youtube.com/watch?v=fokDF4th0IY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=72

# Entrada e Processamento de dados:
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4

# Saída de dados:
print('A média de idade do grupo é de {} anos.'.format(int(mediaIdade)))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho.capitalize()))
print('Ao todo, são {} mulheres com menos de 20 anos'.format(totMulher20))
