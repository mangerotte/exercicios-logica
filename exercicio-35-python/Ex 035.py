"""35) Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo."""

r1 = float(input('Digite a primeira reta do triangulo: '))
r2 = float(input('Digite a segunda reta do triangulo: '))
r3 = float(input('Digite a terceira reta do triangulo: '))

if (r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print('Com os valores apresentados, é possivel formar um triangulo!')
else:
    print('Com esses valores não é possivel formar um triangulo!')