#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
  print('='*40)
  print('ANALISANDO VALORES PASSADOS... ')
  for n in num:
    print(n, end = ' ')
  print(f'Foram digitados {len(num)} valores')
  print(f'O maior valor é {max(num)}')
# programa principal
maior(2,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)