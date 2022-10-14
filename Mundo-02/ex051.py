# https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=67

# Entrada de dados:
termo = (int(input('Primeiro termo: ')))
razao = (int(input('Digite a razão: ')))
decimo = termo + (10-1) * razao

# Processamento e Saída de dados:
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' ')
