#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(lista)
print(impares)
print(pares)