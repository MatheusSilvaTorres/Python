#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=' * 40)
print('{:^40}'.format('Listagem de compras'))
print('=' * 40)
listagem = ('Arroz', 5, 'Feijão', 8, 'Pão', 1, 'Pizza', 15, 'carne', 30, 'ovo', 5, 'bombom', 12)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ') #:30 não foi usado, mas mostra a variavel com 30 caracteres
    else:
        print(f'R${listagem[pos]:>5.2f}') # alinha para direita em 5 posições e deixa as casas decimais certas