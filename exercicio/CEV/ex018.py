"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
v = 0
print('Vamos jogar par ou impar')
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'jogador escolheu {jogador} e computador escolheu {computador} o total foi {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('JOGADOR VENCEU!')
            v += 1
        else:
            print('JOGADOR PERDEU')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('JOGADOR VENCEU!')
            v += 1
        else:
            print('JOGADOR PERDEU!')
            break
    print('Vamos Jogar Novamente!')
print(f'Você ganhou {v} vezes')