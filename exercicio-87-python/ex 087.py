"""87) Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacoluna = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacoluna += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha é {maior}')
