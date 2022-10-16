# https://www.youtube.com/watch?v=BWAWq7n6PCk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=79

# Entrada de dados:
primeiro = (int(input('Primeiro termo: ')))
razao = (int(input('Digite a razão: ')))

# Processamento e Saída de dados:
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada com {} termos mostrados.'.format(total))
