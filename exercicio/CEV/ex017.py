"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."""

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
tot = 0
quantidade = 10
while quantidade != 0:
    tot += quantidade
    while cont <= tot:
        print(termo, end='--> ')
        termo += razao
        cont += 1
    print('Pausa')
    quantidade = int(input('Digite a quantidade que deseja adiconar  a PA: '))
print('Finalizado, foram mostrados {} termos'.format(tot))