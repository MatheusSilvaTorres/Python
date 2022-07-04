"""Faça um programa que leia dois números e mostre um menu com as seguintes opções:
[1] Somar [2] Subtrair [3] Dividir [4] Multiplicar [5] Sair do programa.

O programa deverá realizar a operação solicitada em cada caso."""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while True: 
  opcao=int(input('[1] Somar [2] Subtrair [3] Dividir [4] Multiplicar [5] Sair do programa.'))
  if opcao ==1:
    print('A soma é: {}'.format(num1 + num2))
  elif opcao ==2:
    print('A subtração é: {}'.format(num1-num2))
  elif opcao ==3:
    print('A divisão é: {}'.format(num1/num2))
  elif opcao == 4:
    print('A multiplicação é: {}'.format(num1*num2))
  elif opcao == 5:
    break
  else:
    print("Opção Invalida!!")