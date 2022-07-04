#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
  if nome == '':
    nome = '<desconhecido>'
  if gols == '':
    gols = 0
  print(f'O jogador {nome} fez {gols} gols no campeonato')

# programa principal
jogador = str(input('Digite o nome do jogador: '))
gol = str(input(f'Quantidade de gols do jogador {jogador}: '))
print('='*50)
ficha(jogador, gol)