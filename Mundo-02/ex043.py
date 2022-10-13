# https://www.youtube.com/watch?v=b7r34za963I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=58

# Entrada de dados:
kg = float(input('Digite o peso (kg): '))
m = float(input('Digite a altura (m): '))

# Processamento de dados:
imc = kg / m**2

# Saída de dados:
print('Seu IMC é {:.1f}, está '.format(imc), end='')
if imc < 18.5:
    print('\033[33mAbaixo do peso.\033[m')
elif 18.5 <= imc < 25:
    print('no \033[32mPeso ideal.\033[m')
elif 25 <= imc < 30:
    print('\033[33mem Sobrepeso.\033[m')
elif 30 <= imc < 40:
    print('\033[31mem Obesidade.\033[m')
else:
    print('\033[31mObesidade mórbida.\033[m')
