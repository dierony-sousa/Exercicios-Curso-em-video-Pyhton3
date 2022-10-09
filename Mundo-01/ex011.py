# https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=20

# Entrada de dados:
larg = float(input('Largura da parede (em metros): '))
alt = float(input('Altura da parede (em metros): '))

# Processamento de dados:
area = alt * larg
tinta = area / 2

# Saída de dados:
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
