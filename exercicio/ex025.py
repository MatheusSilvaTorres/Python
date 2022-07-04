#Faça um programa que crie uma lista com 9 números inteiros, compute e mostre os números primos e suas respectivas posições


numeros = []
div = 0
while True:
  try:
    num = int(input('Digite um número inteiro: '))
    if num not in numeros:
      numeros.append(num)
      # print(f'Número {num} adicionado com sucesso')
    if len(numeros) == 9:
      break
  except:
      print('Digite um número válido!')
for index, n in enumerate(numeros):
  tot = 0
  for i in range(1, n+1):
    if n % i == 0:
      tot +=1
  if tot == 2: print(f'O {n} é primo e seu index é {index}')