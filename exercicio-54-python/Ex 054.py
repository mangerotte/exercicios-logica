from datetime import date

"""54) Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

maior = 0
menor = 0
for x in range(0,7):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    if idade > 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas atingiram a maior idade e {menor} não atingiram a maior idade')