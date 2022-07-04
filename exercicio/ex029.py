"""Faça um programa em que o usuário deverá digitar os nomes de dez alunos da sala de aula. Em seguida, caso o programa encontre nomes repetidos, ele deverá alterar o nome adicionando o número sequencial. Por exemplo, se na lista tivermos dois "José", após o processamento a lista deverá conter "José 1" e "José 2".
"""

nomes = []

for i in range(5):
  nome = input('Digite o nome: ')
  nomes.append(nome)
  
for i in range(4):
  
  nome = nomes[i]
  
  if nomes.count(nome) == 1:
    continue    
  
  nomes[i] = nomes[i] + "1"
  contador = 2
  
  for j in range(i+1, 5):
    if nome == nomes[j]:
      nomes[j] = nomes[j] + str(contador)
      contador += 1
      
print(nomes)