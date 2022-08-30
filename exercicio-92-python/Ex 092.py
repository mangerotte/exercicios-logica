from datetime import date

"""92) Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

trabalhador = {}

trabalhador["Nome"] = input('Digite o nome: ')
ano_nascimento = int(input("Digite o ano de nascimento: "))
trabalhador["Idade"] = date.today().year - ano_nascimento
trabalhador["CTPS"] = int(input('Digite o número da Carteira de Trabalho (0 não tem): '))


if trabalhador["CTPS"] != 0:
    trabalhador["Ano Contratação"] = int(input('Digite o ano de contratação: '))
    trabalhador["Sálario"] = float(input('Digite o valor do salário: R$ '))
    trabalhador["Aposentadoria"] = (trabalhador["Ano Contratação"] + 30) - ano_nascimento

for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')