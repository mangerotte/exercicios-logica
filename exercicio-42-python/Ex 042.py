"""42) Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

r1 = float(input('Digite a primeira reta do triangulo: '))
r2 = float(input('Digite a segunda reta do triangulo: '))
r3 = float(input('Digite a terceira reta do triangulo: '))

if (r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print('Com os valores apresentados, é possivel formar um triangulo!')
    if r1 == r2 == r3:
        print('Este triângulo é Equilátero!')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Este triângulo é Isósceles!')
    else:
        print('Este triângulo é Escaleno')
else:
    print('Com esses valores não é possivel formar um triangulo!')