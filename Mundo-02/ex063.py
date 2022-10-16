# https://www.youtube.com/watch?v=w7yn1_Mfu0E&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=80

# Entrada de dados:
n = int(input('Quantos termos da sequencia de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1

# Processamento e Saída de dados:
print('{} {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')
