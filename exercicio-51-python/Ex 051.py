"""51) Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = []

for x in range(pt, 10 * razao, razao):
    pa.append(x)

print(pa)