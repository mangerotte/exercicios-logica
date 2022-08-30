"""96) Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno."""

def terreno(l, c):
    a = l * c
    print(f'A área do terreno {l}x{c} é de {a}m²')


terreno(float(input("Digite a largura: ")), float(input("Digite o comprimento: ")))
