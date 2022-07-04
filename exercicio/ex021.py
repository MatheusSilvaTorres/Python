"""Faça um programa que mostre a tabuada de um número informado."""

n = int(input('Digite um número para ver sua tabuada: '))
print('=' * 20)
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n*i))
print('=' * 20)