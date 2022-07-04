#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


numeros = list()
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para adicionar a lista na posição {c}: ')))
    if c == 0:
      menor = maior = numeros[c]
    else:
      if numeros[c] > maior:
        maior = numeros[c]
      elif numeros[c] < menor:
        menor = numeros[c]

print(f'o maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(numeros):
  if v == maior:
    print(f'{i}...', end='')
print(f'o menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(numeros):
  if v == menor:
    print(f'{i}...', end='')


# print(f'O maior valor foi {max(numeros)} e está na posição {numeros.index(max(numeros))}')
# print(f'O menor valor foi {min(numeros)} e está na posição {numeros.index(min(numeros))}')
