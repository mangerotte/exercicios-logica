"""63) Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci."""

f = int(input('Digite um número inteiro: '))

c = 0
ultimo = 1
penultimo = 1

while c < f-2:
    if c < 1:
        print(ultimo)
        print(penultimo)
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo)
    c += 1