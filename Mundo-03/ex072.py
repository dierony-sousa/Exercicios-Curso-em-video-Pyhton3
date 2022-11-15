# https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=91

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente! ', end='')
print(f'Você digitou o número {extenso[num]}.')
