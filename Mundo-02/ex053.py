# https://www.youtube.com/watch?v=5VBWe6BXzRo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=69

# Entrada de dados:
frase = str(input('Digite uma frase: ')).strip().upper()

# Processamento e Saída de dados:
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
