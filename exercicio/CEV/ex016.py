"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
vezes = 10
soma = 0
while vezes > 0:
    print(soma + termo, end ='--> ')
    soma += razao
    vezes -= 1
print('Acabou!')