#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim= []
while True:
  nome = str(input('Nome: ')).strip().capitalize()
  nota1 = float(input('Nota1: '))
  nota2 = float(input('Nota2: '))
  media = (nota1 + nota2) / 2
  boletim.append([nome, [nota1, nota2], media])
  resp = ' '
  if resp not in 'SN':
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if resp == 'N':
    break
print('='*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('='*30)
for i, aluno in enumerate(boletim):
  print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
  print('='*30)
  opc = int(input('Deseja mostrar as notas de qual aluno[999 P/ SAIR]: '))
  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc <= len(boletim) - 1:
    print(f'O aluno {boletim[opc][0]} tirou as notas {boletim[opc][1]}')