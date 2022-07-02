# Supondo que queremos pintar o muro da instituição, faça um programa que leia a altura e a largura do muro e mostre a quantidade de tinta necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).

altura = int(input("digite a altura do muro:"))
largura = int(input("digite a largura do muro:"))
area = altura * largura
quant = area /2
print("quantidade de tintas:", quant)