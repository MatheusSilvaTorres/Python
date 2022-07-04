"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

mediaIdade = 0
maisVelho = 0
soma = 0
menor = 0
for i in range(1, 5):
    nome = str(input('Digite seu nome ---------- {}° ---------- pessoas: '.format(i))).strip().upper()
    idade = int(input("Digite sua idade: "))
    sexo = str(input('[M/F]')).upper()
    mediaIdade = idade + mediaIdade
    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome
    elif sexo == 'F':
        if idade > 20:
            soma = soma + 1
        else:
            menor += 1
print('A média de idades é: {} \n O homem mais velho possuem {} anos e se chama {}  \n A quantidade de mulheres acima de 20 anos é igual{} \n A quantidade de mulheres menores de idade é igual{}'.format(mediaIdade/4, maisVelho, nomeMaisVelho, soma, menor))