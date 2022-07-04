#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente  são {lista}')
if 5 in lista:
    print(f'Você digitou o valor 5')
else:
    print('Valor 5 não encontrado na lista')