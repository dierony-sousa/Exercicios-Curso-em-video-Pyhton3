# https://www.youtube.com/watch?v=I-SH3QchuZ4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=59

# Entrada de dados:
valBruto = float(input('Digite o valor do produto: R$ '))
print('''Escolha uma das condições de pagamento abaixo:
[1] À VISTA no dinheiro ou cartão.
[2] À VISTA no cartão.
[3] Em até 2X no cartão.
[4] Em 3X ou mais no cartão.''')
condicao = int(input('Digite a condição de pagamento escolhida: '))

# Processamento e Saída de dados:
if condicao == 1:
    desc = valBruto*(10/100)
    valFinal = valBruto - desc
    print('Você teve um desconto de 10%! -R${:.2f}, seu produto ficou em R$ {:.2f}'.format(desc, valFinal))
elif condicao == 2:
    desc = valBruto*(5/100)
    valFinal = valBruto - desc
    print('Você teve um desconto de 5%! -R${:.2f}, seu produto ficou em R$ {:.2f}'.format(desc, valFinal))
elif condicao == 3:
    valFinal = valBruto
    valParc = valBruto / 2
    print('Seu produto ficou em R$ {:.2f}, dividido em 2 parcelas de R$ {:.2f}'.format(valFinal, valParc))
elif condicao == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    if parcelas < 3:
        print('Erro! Selecione uma opção válida para pagar em menos de 3 parcelas!')
    else:
        juros = valBruto * (20/100)
        valFinal = valBruto + juros
        valParc = valFinal / parcelas
        print('Seu produto ficou em R$ {:.2f}, dividdo em {} parcelas de R$ {:.2f}'.format(valFinal, parcelas, valParc))
else:
    print('Erro! Digite uma opção válida!')
