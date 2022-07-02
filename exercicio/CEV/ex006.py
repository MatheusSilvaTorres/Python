# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
catedo_oposto = float(input('Digite o catedo oposto: '))
catedo_adjacente = float(input('Digite o catedo adjacente: '))
hipotenusa = hypot(catedo_oposto, catedo_adjacente)
print('A Hipotenusa é: {:.2f}'.format(hipotenusa))