# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input('Digite um número para verificar se é ímpar ou par: '))

if num%2 == 0:
    print('Esse número é par!')
if num%2 != 0:
    print('Esse número é ímpar')
else:
    print('Na proxima tentativa digite apenas números!')
    