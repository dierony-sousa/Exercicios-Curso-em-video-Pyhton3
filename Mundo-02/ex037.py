# https://www.youtube.com/watch?v=B3F0IjH5WAM&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=52

# Entrada de dados:
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

# Processamento e saída de dados:
if opcao == 1:
    print('{} convertido para \033[34mBINÁRIO\033[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para \033[34mOCTAL\033[m é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para \033[34mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção \033[31mINVÁLIDA!\033[m Tente novamente.')
