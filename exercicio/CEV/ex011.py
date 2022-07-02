# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome possui {} letras A.'.format((nome.lower().count('a'))))
print('Primeiro A apareceu na posição: {}'.format(nome.lower().find('a')+1))
print('Ultimo A apareceu na posição: {}'.format(nome.lower().rfind('a')))