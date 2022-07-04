#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
gols = []
jogadores = []
while True:
  jogador.clear()
  jogador['nome'] = str(input('Nome do jogador: '))
  partidas = int(input(f'Quantadas partidas o {jogador["nome"]} jogou: '))
  gols.clear()
  for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
  jogador['Gols'] = gols[:]
  soma = sum(gols)
  jogador['total gols'] = soma
  jogadores.append(jogador.copy())
  while True:
    resp = str(input('Deseja continuar [S/N]: ')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Digite S ou N')
  if resp == 'N':
    break
print('=' * 50)
print('cod', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('=' * 50)
for k, v in enumerate(jogadores):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('=' * 50)
while True:
  busca = int(input('Mostrar dados de qual jogador? [999 p/ sair]'))
  if busca == 999:
    break
  if busca >= len(jogadores):
    print('Jogador não encontrado com esse número')
  else: 
    print(f'Levantamento do jogador {jogadores[busca]["nome"]}')
    for i, gol in enumerate(jogadores[busca]["Gols"]):
      print(f'   No jogo {i+1} fez {gol} gols')
  print('=' * 50)
print('Finalizado')
