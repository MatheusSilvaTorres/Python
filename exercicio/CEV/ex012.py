# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
nome1 = nome.split()
print('muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome1[0]))
print('seu ultimo nome é {}'.format(nome1[-1]))
#print('seu ultimo nome é {}'.format(nome1[len(nome1)-1]))