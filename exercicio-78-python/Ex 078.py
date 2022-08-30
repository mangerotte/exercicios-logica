"""78) Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista = []
menor = maior = 0
pmaior = 0
pmenor = 0
for c in range(0,6):
    n = int(input(f'Digite um número na posição {c}: '))
    lista.append(n)
    if c < 1:
        menor = n
        pmenor = c
        maior = n
        pmaior = c
    if n < menor:
        menor = n
        pmenor = c
    elif n > maior:
        maior = n
        pmaior = c
print(f'Os valores da lista são {lista}, e o menor valor é {menor} na posição {pmenor} e o maior valor é {maior} na posição {pmaior}')
