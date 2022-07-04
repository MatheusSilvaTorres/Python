#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint
palpites = list()
jogos = []
tot = 0
print('=' *30)
print('     PALPILTE DA MEGA-SENA    ')
print('='*30)
quantidade = int(input('Quantos jogos deseja fazer: '))
print('='* 5, f' SORTEANDO {quantidade} JOGOS','='*5 )
while tot < quantidade:
  cont = 0
  while True:
    num = randint(1, 60)
    if num not in palpites:
      palpites.append(num)
      cont+= 1
    if cont >= 6:
      break
  palpites.sort()
  jogos.append(palpites[:])
  palpites.clear()
  tot += 1
for i, l in enumerate(jogos):
  print(f'Jogo {i+1}º: {l} ')
  sleep(1)
