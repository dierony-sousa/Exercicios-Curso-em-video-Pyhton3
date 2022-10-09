# https://www.youtube.com/watch?v=KjcdG05EAZc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=17

# Entrada de dados:
valMetro = float(input('Uma distância em metros: '))

# Saída de dados:
print('A medida de {}m, corresponde a:'.format(valMetro))
print('{} km (quilômetro)'.format(valMetro/1000))
print('{} hm (hectômetro)'.format(valMetro/100))
print('{} dam (decâmetro)'.format(valMetro/10))
print('{} dm (decímetro)'.format(valMetro*10))
print('{} cm (centímetro)'.format(valMetro*100))
print('{} mm (milímetro)'.format(valMetro*1000))
