"""33) Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))


if n1 > n2 and n3:
    print(f'O maior numero é {n1}')
    if n2 < n3:
        print(f'O menor numero é {n2}')
    else:
        print(f'O menor numero é {n3}')

elif n2 > n1 and n3:
    print(f'O maior numero é {n2}')
    if n1 < n3:
        print(f'O menor numero é {n1}')
    else:
        print(f'O menor numero é {n3}')

elif n3 > n1 and n2:
    print(f'O maior numero é {n3}')
    if n1 < n2:
        print(f'O menor numero é {n1}')
    else:
        print(f'O menor numero é {n2}')