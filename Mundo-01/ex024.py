# https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=35

# Entrada de dados:
city = str(input('Digite o nome de uma cidade: ')).strip()

# Processamento e saída de dados:
print('O nome da cidade começa com "Santo"?', end=' ')
print(city[:5].capitalize() == 'Santo')
