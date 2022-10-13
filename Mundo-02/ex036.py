# https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=51

# Entrada de dados:
valCasa = float(input('Qual é o valor da casa? R$ '))
salComp = float(input('Qual é o salário do comprador? R$ '))
anos = int(input('Pretende pagar a casa em quantos anos? '))

# Processamento de dados:
prestMensal = valCasa / (anos*12)
valCred = salComp * (30/100)

# Saída de dados:
print('Para pagar uma casa de R${:.2f}, em {} anos, o valor da pretação mensal será de R${:.2f}.'.format(valCasa, anos, prestMensal))

if prestMensal <= valCred:
    print('Empréstimo \033[32mAPROVADO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\033[m O salário do comprador ficou comprometido em mais de 30%.')
