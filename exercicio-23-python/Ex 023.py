"""23) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

n = int(input('Digite um numero de 0 a 9999: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milha = n // 1000 % 10

print(f'Analisando o numero {n}')
print(f'Unidade = {unidade}')
print(f'Dezena = {dezena}')
print(f'Centena = {centena}')
print(f'Milhar = {milha}')