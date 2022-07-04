#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))
print(f'O nome é {aluno["nome"]}')
print(f'A media é {aluno["media"]}')
if aluno['media'] > 7:
  aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
  aluno['situação'] = 'Recuperação'
else:
  aluno['situação'] ='Reprovado'
print(f'A situação é {aluno["situação"]}')