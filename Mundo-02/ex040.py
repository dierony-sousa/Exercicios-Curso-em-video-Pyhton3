# https://www.youtube.com/watch?v=QuWDyUeoaJs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=55

# Entrada de dados:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Processamento de dados:
media = (n1 + n2) / 2

# Saída de dados:
if media >= 7:
    print('A média foi {:.1f}, aluno está \033[32mAPROVADO!\033[m'.format(media))
elif media < 5:
    print('A média foi {:.1f}, aluno está \033[31mREPROVADO!\033[m'.format(media))
else:
    print('A média foi {:.1f}, aluno está de \033[33mRECUPERAÇÃO!\033[m'.format(media))
