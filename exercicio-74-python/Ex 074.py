from random import randint

"""74) Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

maior = 0
menor = 0
count = 0

while count <= 5:
    for c in n:
        if count <= 1:
            menor = c
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
        count += 1
print(n)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')