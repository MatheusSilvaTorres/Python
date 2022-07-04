#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
anoAtual = date.today().year
trabalhador = dict()
trabalhador['Nome'] = str(input('Qual seu nome: '))
anoNasc = int(input('Ano do seu nascimento: '))
trabalhador['Idade'] = anoAtual - anoNasc
print(trabalhador)
trabalhador['CPTS'] = int(input('Carteira de trabalho [0 Não tem]'))
if trabalhador['CPTS'] != 0:
  trabalhador['Contratação'] = int(input('Ano de contratação: '))
  trabalhador['Salario'] = float(input('Salário: '))
  trabalhador['Aposentadoria'] = trabalhador['Contratação'] + 35 - anoNasc
for k,v in trabalhador.items():
  print(f'O {k} tem valor {v}')