"""Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor (não utilize as funções built-in max() e min())"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
  print('O número maior é: {}'.format(num1))
elif num2 > num3:
  print('O número maior é: {}'.format(num2))
else: 
  print('O número maior é: {}'.format(num3))

if num1 < num2 and num1 < num3:
  print('O número menor é: {}'.format(num1))
elif num2 < num3:
  print('O número menor é: {}'.format(num2))
else: 
  print('O número menor é: {}'.format(num3))