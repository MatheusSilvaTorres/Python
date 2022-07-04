"""Implemente o jogo da forca. Um usuário deverá entrar com uma palavra. Em seguida, outro usuário deverá indicar as letras dessa palavra. Caso exista, deverá ser mostrada as letras e as suas posições na palavra. Caso não exista, o usuário perderá uma chance. No total, o usuário terá 6 chances para acertar.
"""

palavra = input('Digite uma palavra: ')

resultado = []
for c in palavra:
  resultado.append('_')

chances = 6

while True:
  
  print(resultado)
  
  letra = input('Digite uma letra: ')
  
  if letra not in palavra:
    chances -= 1
  else:
    for index, l in enumerate(palavra):
      if l == letra:
        resultado[index] = l    
    
  if chances == 0:
    print('Game Over')
    break
    
  if resultado.count('_') == 0:
    print('Parabéns!')
    break