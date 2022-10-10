# https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=46

# Entrada de dados:
sal = float(input('Digite o salário do funcionário: R$'))

# Processamento de dados:
if sal > 1250:
    sal = sal + sal*10/100
else:
    sal = sal + sal*15/100

# Saída de dados:
print('O novo salário do funcionário é R${:.2f}'.format(sal))
