"""57) Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""

while True:
    sexo = input('Digite o seu sexo [M] Masculino e [F] Feminino: ').upper()
    if sexo == 'M':
        print('O seu sexo é masculino!')
    elif sexo == 'F':
        print('O seu sexo é feminino!')
    else:
        print('Digite apenas M ou F!')