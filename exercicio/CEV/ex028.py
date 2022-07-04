# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite uma expressão matematica: '))
pilha = list()
for simbolo in expressão:
  if simbolo == '(':
    pilha.append('(')
  elif simbolo == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua expressão está correta!')
else: 
  print('Sua expressão está inválida!')
