"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

Input: 5

Output: 120"""

num = int(input('Digite um número: '))
fatorial = num
while num > 1:
  num -= 1
  fatorial = fatorial * num
print(fatorial)