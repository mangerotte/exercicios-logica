"""86) Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[], [], []]
temp = []
for c in range(0, 3):
    temp.append(int(input(f'Digite um valor para [0,{c}]: ')))
    matriz[0].append(temp[:])
    temp.clear()
for c in range(0,3):
    temp.append(int(input(f'Digite um valor para [1,{c}]: ')))
    matriz[1].append(temp[:])
    temp.clear()
for c in range(0,3):
    temp.append(int(input(f'Digite um valor para [2,{c}]: ')))
    matriz[2].append(temp[:])
    temp.clear()

print(f'{matriz[0][0].center(5)} {matriz[0][1].center(5)} {matriz[0][2].center(5)}')
print(f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}')
print(f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}')