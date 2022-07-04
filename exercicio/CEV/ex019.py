"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato."""

soma = cont = menor = maior = 0
produto = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    soma += preco
    cont += 1
    if preco > 1000:
        maior += 1
    if cont == 1 or preco < menor:
        menor = preco
        produto = nome
    resp = str(input('Deseja cotinuar [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja cotinuar [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total gasto foi R$ {soma:.2f}')
print(f'Tem {maior} produtos que custam mais de R$ 1.000,00')
print(f'O produto mais barato è {produto} e custa {menor:.2f}')
print(f'Foram processados {cont} produtos ')