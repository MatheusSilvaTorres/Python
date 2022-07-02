# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
print('Vamos verificar anos bissextos!')
ano = int(input('Qual ano deseja verificar?'))''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} é bissexto!')
else: 
  print(f'O ano {ano} não é bissexto!')