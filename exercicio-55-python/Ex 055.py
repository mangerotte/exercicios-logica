"""55) Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso digitado foi {maior} kg e o menor peso foi de {menor} kg')