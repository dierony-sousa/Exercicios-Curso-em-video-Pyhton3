# https://www.youtube.com/watch?v=NR1RKt6NT8s&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=62

from time import sleep

# Processamento e Saída de dados:
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[33mBoom! \033[32mBoom \033[35mPô! Pô! Pô! \033[36mBoom! \033[m')
