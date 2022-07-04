"""Faça um programa que leia um número inteiro N e mostre na tela os N primeiros números da Sequência de Fibonacci.
Input: 7

Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""

numero = int(input("digite um número: "))
contador = 1
a = 1
b = 0

print("{} ->".format(b), end=' ')

while numero > contador:
  
  soma = a + b
  print("{} ->".format(soma), end=' ')
  a = b
  b = soma
  
  contador = contador + 1 #contador += 1