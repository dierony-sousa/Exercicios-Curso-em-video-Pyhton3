# https://www.youtube.com/watch?v=d2ug6quC1bk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=84

cont = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para PARAR]: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'No total foram informados {cont} e a SOMA entre eles é {soma}.')
