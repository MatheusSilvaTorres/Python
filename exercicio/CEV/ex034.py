#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
for i in range(1, 4):
  jogadores[f'Jogador {i}'] = randint(1, 6)
print('sorteando valores')
for k, v in jogadores.items():
  print(f'O {k} tirou {v}')
  sleep(1)
ranking = []
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True )
print('Ranking Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} ')
    sleep(1)