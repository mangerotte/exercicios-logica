"""50) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""

s = 0

for x in range(0, 6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        s += n1


print(f'O valor total de números pares é {s}')