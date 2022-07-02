# Faça um programa que leia o preço de um produto e mostre o valor com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
print('Novo preço do produto é: {:.2f}'.format(preco - preco*0.05))