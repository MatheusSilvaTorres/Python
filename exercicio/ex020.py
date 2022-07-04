"""Faça um programa que leia um número inteiro e mostre na tela se é ou não um número primo."""

soma = 0
n = int(input('Digite um número: '))
for i in range(1, n+1):
    if n % i == 0:
        print('\033[34m', end=' ')
        soma = soma + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
if soma == 2:
    print('\033[30m O número {} é um número primo'.format(n))
else:
    print('\033[30m O número {} não é um número primo'.format(n))