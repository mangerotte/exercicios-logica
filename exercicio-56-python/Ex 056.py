"""56) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

homem_velho = ''
idade_homem_velho = 0
mulheres_menor = 0
contador_idade = 0

for c in range(0,4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M] mascluno e [F] para feminino: ')

    contador_idade += idade

    if sexo == 'M':
        if idade_homem_velho < idade:
            idade_homem_velho = idade
            homem_velho = nome

    if sexo == 'F':
        if idade < 20:
            mulheres_menor += 1

media = contador_idade / 4

print('-=-'*20)
print(f'''A média de idade do grupo é de {media:.2f}
O homem mais velho é o {homem_velho}
Existe {mulheres_menor} mulheres com menos de 20 anos neste grupo!''')

