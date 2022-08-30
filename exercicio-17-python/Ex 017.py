"""17) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa."""

import math

coposto = int(input('Digite o valor do cateto oposto: '))
cadjacente = int(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(coposto, 2) + math.pow(cadjacente,2))
print(f'O valor da hipotenusa é {hipotenusa}')


