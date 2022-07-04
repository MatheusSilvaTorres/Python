"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input(('Digite seu peso da {}° pessoa: '.format(pessoas))))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O peso maior é: {} \n O peso menor é: {}'.format(maior, menor))