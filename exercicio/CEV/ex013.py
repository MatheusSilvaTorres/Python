# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint
num = randint(0, 5)
print('\33[34m--=--' * 20)
print('\33[35mVou pensar em um número entre 0 e 5. Tente adivinhar.')
print('\33[34m --=--' * 20)
escolha = int(input('Em que número pensei: '))
print('\33[32m PROCESSANDO...')
sleep(3)
if escolha == num:
    print('\33[32m Você acertou! PARABÉNS')
else:
    print('\33[31m Eu VENCI pensei no número {} e não no {}'.format(num, escolha))

