"""Faça um programa para jogar Jokenpô (clássico pedra, papel e tesoura) com você. Você deverá informar uma das opções, o programa deverá então sortear uma das três opções possíveis e mostrar quem ganhou na tela."""

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('o computador escolheu: {}'.format(itens[computador]))
print('suas opções [0] pedra, [1] papel, [2] tesoura')
jogador = int(input('Qual sua jogada: '))
print('o jogador escolheu: {}'.format(itens[jogador]))

if computador == 0:
  if jogador == 0:
    print('Empate')
  elif jogador == 1:
    print('jogador ganhou')
  elif jogador == 2:
    print('computador ganhou')
elif computador == 1:
  if jogador == 0:
    print('computador venceu')
  elif jogador == 1:
    print('Empate')
  elif jogador == 2:
    print('Jogador ganhou')
elif computador == 2:
  if jogador == 0:
    print('Jogador ganhou')
  elif jogador == 1:
    print('computador venceu')
  elif jogador == 2:
    print('empate')
