#Crie uma função que receba com parâmetro o nome, email e telefone de uma pessoa (sendo este último opcional). Em seguida, retorne os dados no formato de um dicionário
def pessoa(nome, email, telefone = None):
  return {'nome': nome, 'email': email, 'telefone': telefone}
  lista(pessoa)

pessoa('matheus Torres', 'matheus_torres')
pessoa('matheus Torres', 'matheus_torres', '1489164')