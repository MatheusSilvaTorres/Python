"""Faça um programa que faça a entrada de um texto. Se for um e-mail, retorne "E-mail válido", caso contrário, retorno "E-mail inválido". Para tanto, verifique se o texto possui o símbolo @ usando a função interna .isalnum()."""

email = input('Digite seu e-mail: ')

for c in email:
  if not c.isalnum() and c == '@':
    print('E-mail válido')
    break
else:
  print('E-mail inválido')