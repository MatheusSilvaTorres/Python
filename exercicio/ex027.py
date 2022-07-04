""" Faça um programa que crie duas listas x e y, com dez números inteiros cada uma. Os valores deverão ser informados pelo usuário e os valores não podem se repetir dentro de uma lista. Em seguida, crie:
Uma lista resultante da união de x e y (todos os elementos de x e os elementos de y que não estão em x).
Uma lista resultante da diferença entre x e y (todos os elementos de x que não existam em y).
Uma lista resultante da some de x e y (soma de cada elemento de x com o elemento de y na mesma posição)
"""

lista_x = list()
lista_y = list()

contador = 0
while contador < 10:  
  numero = int(input('Digite um número: '))  
  if numero not in lista_x:
    lista_x.append(numero)
    contador += 1
    
contador = 0
while contador < 10:  
  numero = int(input('Digite um número: '))  
  if numero not in lista_y:
    lista_y.append(numero)
    contador += 1  
# A
lista1 = lista_x.copy()
for n in lista_y:
  if n not in lista_x:
    lista1.append(n)

# B
lista2 = lista_y.copy()
for n in lista_x:
  if n not in lista_y:
    lista2.append(n)

# C
lista3 = list()
for i in range(0,10):
  soma = lista_x[i] + lista_y[i]
  lista3.append(soma)

print(lista1)
print(lista2)
print(lista3)