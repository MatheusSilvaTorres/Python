"""Faça um program que leia o ano de nascimento de uma pessoa e informe se ele ainda vai se alistar ao serviço militar ou se ele está no período de se alistar ou se ele perdeu o prazo para se alistar. Além disso, mostre também a quantidade de anos que falta para se alistar ou que passou do prazo."""


from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc
if idade == 18:
    print('Está na hora de se alistar!!')
elif idade > 18:
    print('Passou do tempo de alistamento em {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoAtual-(idade-18)))
else:
    print('Falta {} anos para se alistar'.format(18 - idade))
    print('Seu alistamento será em {}'.format(anoNasc + 18))