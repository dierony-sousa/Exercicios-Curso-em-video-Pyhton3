# https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=22

# Entrada de dados:
sal = float(input('Qual é o salário do funcionário? R$'))

#Processamento de dados:
novoSal = sal + (sal*(15/100))

# Saída de dados:
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, novoSal))
