# https://www.youtube.com/watch?v=Qp2cXfCHk2I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=96

cesta_basica = ('Arroz 5Kg', 21.49, 'Feijão Carioca 1kg', 9.29,
                'Óleo de Soja', 7.89, 'Sal Refinado', 3.99,
                'Açúcar Cristal 5kg', 15.99, 'Café Tradicional 500g', 16.48,
                'Extrato de Tomate', 3.89, 'Macarrão Espaguete 500g', 4.39,
                'Sardinha', 5.99, 'Salsicha (lata)', 5.69, 'Milho (lata)', 3.39,
                'Farinha de Trigo', 5.99, 'Biscoito 500g', 5.99,
                'Pão de Forma', 9.99, 'Margarina 250g', 5.69, 'Banana (penca)', 8.39,
                'Leite em Pó 300g', 16.99)
print('-'*49)
print(f'{"Listagem de preços da Cesta Básica | 2022":^50}')
print('-'*49)
for pos in range(0, len(cesta_basica)):
    if pos % 2 == 0:
        print(f'{cesta_basica[pos]:.<41}', end='')
    else:
        print(f'R${cesta_basica[pos]:>6.2f}')
print('-'*49)
