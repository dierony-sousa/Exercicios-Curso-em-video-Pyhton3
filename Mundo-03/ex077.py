# https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=96&t=293s

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'cursto', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')
