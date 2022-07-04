#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada

from time import sleep
def contador (inicio, fim, passo):
  if passo == 0:
    passo = 1
  if passo < 0:
    passo = passo * - 1
  print('=' * 50)
  print(f'contagem de {inicio} até {fim} contando de {passo} em {passo}')
  if inicio < fim:
    cont = inicio
    while cont <= fim:
      print(f'{cont}', end= ' ', flush = True)
      sleep(0.25)
      cont += passo
  else:
    cont = inicio
    while cont >= fim:
      print(f'{cont}', end= ' ', flush = True) # flush foi usado pois no pycharme estava mostrando sem esperar o tempo
      sleep(0.25)
      cont -= passo 
  print('FIM')
   
#programa principal
contador(1,10,1)
contador(10,0,2)
print('AGORA É SUA VEZ DE PERSONALIZAR!!!')
começo = int(input('inicio: '))
final = int(input('fim: '))
passos = int(input('passo: '))
contador (começo, final, passos)