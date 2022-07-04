"""Faça um programa que carregue duas listas com nomes de animais, com 5 posições cada lista. Em seguida, crie uma lista resultante da intercalação dessas duas listas. No final, mostre os itens dessa nova lista.
"""

lista1 = ['cachorro', 'gato', 'pato', 'macaco', 'papagaio']
lista2 = ['jacaré', 'lobo', 'boi', 'vaca', 'ovelha']


lista3 = []

for i in range(0, 5):
  lista3.append(lista1[i])
  lista3.append(lista2[i])