"""Exercício 9: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens:
O primeiro valor é maior.
O segundo valor é maior.
Os valores são iguais."""

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if a > b:
  print('{} é o maior valor'. format(a))
elif b > a:
  print('{} é o maior valor'. format(b))
else:
  print('Os valores são iguais')