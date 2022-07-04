# melhorando o desafio da escolha
from time import sleep
from random import randint
tentativas = 0
acertou = False
num = randint(0, 10)
print('\33[34m --=--' * 20)
print('\33[35mVou pensar em um número entre 0 e 10. Tente adivinhar.')
print('\33[34m --=--' * 20)
while not acertou:
    jogador = int(input('\33[m Em que número pensei: '))
    tentativas += 1
    print('\33[32m PROCESSANDO...')
    sleep(1)
    if jogador == num:
        acertou = True
    if jogador == num:
        print('\33[32m Você acertou! PARABÉNS. Com {} tentativas!'.format(tentativas))
    else:
        if num > jogador:
            print('\33[31m Mais....')
        else:
            print('\33[31m Menos....')