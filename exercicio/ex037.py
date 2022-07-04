#Crie uma função que receba uma quantidade indefinida de números e retorne seus valores multiplicados por um parâmetro definido obrigatóriamente.

def mutiplicacao(*args, mutiplicador = 3):
  lista = []
  for n in args:
    n = n * mutiplicador
    lista.append(n)
  print(lista)
mutiplicacao(4,5,6,8)