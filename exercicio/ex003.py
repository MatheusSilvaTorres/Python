# Implemente um programa que leia 4 notas de um aluno e mostre a média aritmética.

n = int(input('Digite um número: '))
print('número: {}, seu dobro: {}, seu triplo: {}, raiz quadrada: {:.2f}'.format(n, n * 2, n * 3, n ** (1 / 2)))
# outra forma de calcular raiz quadrada
print(pow(n, (1/2)))