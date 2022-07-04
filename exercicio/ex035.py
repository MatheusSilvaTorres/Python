#Faça um programa que tenha uma função chamada "maior", a qual poderá receber diversos parâmetros do tipo inteiro. O programa deverá retornar o maior número.

def maior(*args):
  print(max(args))
maior(1,56,8,2,4)