#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in numeros:
        numeros.append(n)
        print('Número cadastrado com sucesso!')
    else:
        print('Valor já cadastrado, tente outro...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(sorted(numeros))
