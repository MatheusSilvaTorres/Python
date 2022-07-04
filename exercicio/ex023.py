"""Você recebe uma string e uma largura. Sua tarefa é envolver a string em um parágrafo com esta largura (text wrapper).
Input: "Texto muito longo", largura: 4

OutPut:

Text

o mu

ito

long

o"""

contador = 1
for c in texto:
  print(c, end='')
  if contador % 4 == 0:
    print('\n')
  contador += 1