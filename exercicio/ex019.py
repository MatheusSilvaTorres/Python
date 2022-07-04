"""Considerando as formatações abaixo para exibir um valor binário e um valor em hexadecimal, crie um programa que receba um número inteiro e mostre de 0 até este número sua representação decimal, binária e hexadecimal.
"{0:b}" binário

"{0:x}" hexadecimal

Input: 11 Output:

0 0 0

1 1 1

2 10 2

3 11 3

4 100 4

5 101 5

6 110 6

7 111 7

8 1000 8

9 1001 9

10 1010 A"""

numero = int(input("Digite um número: "))

for i in range(numero):
  print("{0} \t {0:b} \t {0:x}".format(i))