"""69) Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

maior_18 = homens = mulheres_20 = 0

while True:
    sexo = ' '
    sair = ' '
    idade = ' '

    while not idade.isdigit():
        idade = input('Digite sua idade: ')
    while sexo not in 'FM':
        sexo = input('Informe seu sexo [M]asculino ou [F]eminino:  ').upper().strip()[0]
    while sair not in 'SN':
        sair = input('Deseja continuar? [S]im [N]ão: ').upper().strip()[0]

    idade = int(idade)
    if sair == 'N':
        break
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

print(f'''Existe {maior_18} pessoas maiores de 18 anos;
Foram cadastrados {homens} homens;
Foram cadastradas {mulheres_20} mulheres com menos de 20 anos.''')