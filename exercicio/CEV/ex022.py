"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

soma = 0
tot = 0
from datetime import date
anoAtual = date.today().year
for i in range(1, 8):
    anoNasc = int(input('Digite seu ano de nascimento da {}ª pessoa: '.format(i)))
    idade = anoAtual - anoNasc
    if idade >= 21:
        soma = soma + 1
    else:
        tot = tot + 1
print('A quantidade de pessoas maiores de idade é {}'.format(soma))
print('A quantidade de pessoas menores de idade é {}'.format(tot))