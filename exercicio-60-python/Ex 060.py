"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input("Fatorial de: ") )

resultado = 1
c = 1

while c <= n:
    resultado *= c
    c += 1

print(resultado)