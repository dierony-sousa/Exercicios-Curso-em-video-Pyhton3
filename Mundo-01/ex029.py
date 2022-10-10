# https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=41

# Entrada de dados:
vel = float(input('O carro está a quantos km/h ? '))

# Processamento e Saída de dados:
if vel > 80.0:
    multakm = 7.00
    dif = vel - 80.0
    multatotal = multakm * dif
    print('Excedeu {} km/h, você foi MULTADO e deve pagar R$ {:.2f}!'.format(dif, multatotal))
else:
    print('Você está dentro do limite de velocidade permitido.')
print('Dirija com segurança! FIM!')
