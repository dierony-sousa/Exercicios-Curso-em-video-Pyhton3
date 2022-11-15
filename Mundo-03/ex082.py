# https://www.youtube.com/watch?v=uk0gDFQEo_I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=102

valores = []
valoPar = []
valImpa = []
while True:
    n = (int(input('Digite um valor: ')))
    valores.append(n)
    if n % 2 == 0:
        valoPar.append(n)
    else:
        valImpa.append(n)
    r = str(input('Quer continuar? [S/N]'))

    if r in 'Nn':
        break
print(f'Lista com todos os valores digitados {valores}.')
print(f'Lista com todos os valores pares {valoPar}.')
print(f'Lista com os valores ímpares: {valImpa}.')
