"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúscula é: {} '.format(nome.upper()))
print('Seu nome em minúscula é: {} '.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) find foi usado para encontrar o primeiro espaço
nome1 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))