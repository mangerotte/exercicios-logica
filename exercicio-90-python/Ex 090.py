"""90) Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
aluno["Nome"] = input('Digite o nome do aluno: ')
aluno["Média"] = float(input(f'Digite a média do {aluno["Nome"]}: '))

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif aluno["Média"] > 5 and aluno["Media"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"
print("-="*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
