"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""

numeros = [[], []]
temporario = []
while True:
    temporario.append(int(input('Digite um numero: ')))
    sair = input('Deseja Continuar? [S]im ou [N]ão: ').upper().strip()

    for n in temporario:
        if n % 2 == 0:
            numeros[0].append(temporario[:])
        else:
            numeros[1].append(temporario[:])
    temporario.clear()
    if sair == 'N':
        break
print("-="*30)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram {sorted(numeros[1])}')