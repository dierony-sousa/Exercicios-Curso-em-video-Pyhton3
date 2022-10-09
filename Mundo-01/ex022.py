# https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=33

# Entrada de dados:
nome = str(input('Digite seu nome completo: ')).strip()

# Saída de dados:
print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
