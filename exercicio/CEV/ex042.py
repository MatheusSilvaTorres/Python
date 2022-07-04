# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def sorteia(numeros = list(), soma = 0):
  for i in range(0, 5):
    numeros.append(randint(1, 10))
  for n in numeros:
    if n % 2 == 0:
      soma += n
  print(f'Foram digitados os valores {numeros} e a soma dos pares é {soma}')
sorteia()