"""Você recebe uma string e sua tarefa é trocar casos. Em outras palavras, converta todas as letras minúsculas em maiúsculas e vice-versa.
Input: Fatec Rio Preto

Output: fATEC rIO pRETO"""

texto = input("Digite um texto: ")
texto_aux = ""

for c in texto:
  
  if c.islower():
    texto_aux = texto_aux + c.upper()
  else:
    texto_aux = texto_aux + c.lower()
    
print(texto_aux)