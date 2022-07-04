#Crie uma função que receba uma quantidade indefinida de números e retorne seus valores multiplicados por 2.

def mutiplicacao(*args):
  lista = []
  for n in args:
    n = n * 2
    lista.append(n)
  print(lista)
mutiplicacao(4,5,6,8)