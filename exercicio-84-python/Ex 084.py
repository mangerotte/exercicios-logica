"""84) Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(input('Digite seu nome: '))
    dados.append(float(input('Digite seu peso: ')))
    sair = input('Deseja Continuar: [S]im [N]ão: ').upper().strip()
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        maior = menor = dados[1]
    dados.clear()

    for p in pessoas:
        if p[1] > maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]

    if sair == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso é {maior} kg. Peso de ', end='')
for p in pessoas:
        if p[1] == maior:
            print(f'{[p[0]]}', end=' ')
print()
print(f'E o menor peso é {menor} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{[p[0]]}', end=' ')
