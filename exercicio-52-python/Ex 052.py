"""52) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

n = int(input('Digite um numero inteiro: '))

multi = 0

for count in range(1,n):
    if n % count == 0:
        multi += 1

if multi == 1:
    print('É um numero primo!')
else:
    print('Não é um numero primo')