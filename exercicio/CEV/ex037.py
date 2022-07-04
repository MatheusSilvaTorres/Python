#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

grupo = list()
mulheres = []
pessoa = dict()
soma =  0
while True:
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo']= str(input('Sexo [M/F]: ')).upper()[0]
    if  pessoa['sexo'] not in 'MF':
      pessoa['sexo']= str(input('Sexo [M/F]: ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Digite apenas M ou F')
  if pessoa['sexo'] == 'F':
      mulheres.append(pessoa['nome'])
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  grupo.append(pessoa.copy())
  pessoa.clear()
  while True:
    resp = str(input('Deseja continuar [S/N]: ')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Digite apenas S ou N')
  if resp in 'N':
    break
print(grupo)
print(f'A) O grupo tem {len(grupo)} pessoas')
print(f'B) A média de idade é {soma / len(grupo):5.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for i, mulher in enumerate(mulheres):
  print(mulher, end= ' ')
print()
print('D) Lista das pessoas que estão acima da media: ', end= '')
for pessoa in (grupo):
  if pessoa['idade'] >= soma/ len(grupo):
    print('    ', end='')
    for k, v in pessoa.items():
      print(f' {k} = {v}: ', end='')
    print()
print('Encerrado')