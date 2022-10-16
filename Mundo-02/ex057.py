# https://www.youtube.com/watch?v=JGztEBLGj5E&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=74

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Iforme o sexo biológico [M/F]: ').strip()).upper()[0].split()
    if sexo == ['M']:
        sexo = 'M'
        print('Você informou sexo:\033[34m MASCULINO\033[m')
    elif sexo == ['F']:
        sexo = 'F'
        print('Você informou sexo:\033[35m FEMININO\033[m')
    else:
        print('\033[31mDados Inválidos! \033[mPor favor, informe uma opção válida!')
