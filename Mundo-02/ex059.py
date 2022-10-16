# https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=76

num1 = int(input('\nInforme o 1º número: '))
num2 = int(input('Informe o 2º número: '))
sair = False

while not sair:
    print('--'*21)
    print('''\033[34mMENU:\033[m
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    menu = int(input('Informe a opção desejada conforme o MENU: '))
    if menu == 1:
        print('\033[32mSOMA:\033[m {} + {} = {}'.format(num1, num2, num1+num2))
    elif menu == 2:
        print('\033[32mMULTIPLICAÇÃO:\033[m {} x {} = {}'.format(num1, num2, num1*num2))
    elif menu == 3:
        if num1 > num2:
            print('\033[32mMAIOR:\033[m {} é MAIOR que {}'.format(num1, num2))
        elif num2 > num1:
            print('\033[32mMAIOR:\033[m {} é MAIOR que {}'.format(num2, num1))
        else:
            print('\033[32mMAIOR:\033[m {} é IGUAL a {}'.format(num1, num2))
    elif menu == 4:
        print('\033[32mNovos números:\033[m')
        num1 = int(input('\nInforme o 1º número: '))
        num2 = int(input('Informe o 2º número: '))
    elif menu == 5:
        sair = True
    else:
        print('Opção \033[31mINVÁLIDA!\033[m')
print('Você \033[33mSAIU\033[m do programa.')
