#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
  for c in range(0, 3):
    valores[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}] '))
print(valores)
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{valores[l][c]:^5}]', end='') # :^5 deixa com 5 casas decimais centralizado
  print() # quebra linha