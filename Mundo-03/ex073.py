# https://www.youtube.com/watch?v=RexybLcGewA&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=92

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Bota Fogo', 'Atlético PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Havaí', 'Ponte Preta', 'Atlético GO')
print('--'*15)
print(f'Os 5 primeiros colocados são: {times[0: 5]}')
print('--'*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('--'*15)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('--'*15)
print(f'O time Chapecoense está na {times.index("Chapecoense")+1}ª posição')
