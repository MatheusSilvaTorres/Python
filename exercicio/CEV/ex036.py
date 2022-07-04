# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantadas partidas o {jogador["nome"]} jogou: '))
for i in range(0, partidas):
  gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
jogador['Gols'] = gols
jogador['total gols'] = sum(gols)
print('=' * 50)
print(jogador)
print('=' * 50)
for k, v in jogador.items():
  print(f'O campo {k} tem valor {v}')
print('=' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, gol in enumerate(gols):
  print(f'Na partida {i+1} fez {gol} gol')
print(f'Foi um total de {jogador["total gols"]} gols')