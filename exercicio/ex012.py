# conversão de números
num = int(input('Digite um número decimal inteiro: '))
print('''escolha umas das opções para conversão
[1] converter para binário
[2] converter para octal
[3] converter para binário''')
opcao = int(input('escolha uma das opções: '))
if opcao == 1:
    print('o número {}, em binário é {}'.format(num, bin(num)[2:])) # fatiamento
elif opcao == 2:
    print('o número {}, em octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('o número {}, em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida!')