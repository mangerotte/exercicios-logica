import random

"""28) Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5,
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu."""


n = int(input('Digite um numero: '))
s = random.randint(0,5)

if n == s:
    print(f'Você acertou o numero que o PC escolheu foi {s}')
else:
    print(f'Você errou! O numero que o PC escolheu foi {s}')
