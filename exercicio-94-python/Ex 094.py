"""Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

dicionario = {}
cadastro = []
mulheres = []
soma = 0


def leiaidade(msg):
    ok = False
    valor = 0
    while True:
        n = input((msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def leianome(msg):
    ok = False
    valor = ""
    while True:
        nome = input((msg))
        valor = nome
        if not nome.isnumeric():
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas letras.\033[m')
        if ok:
            break
    return valor

def leiasexo(msg):
    ok = False
    valor = ""
    while True:
        sexo = input((msg)).upper().strip()
        valor = sexo
        if sexo in "MF":
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas a letra "M" ou "F".\033[m')
        if ok:
            break
    return valor
def leiasair(msg):
    ok = False
    valor = ""
    while True:
        sair = input((msg)).upper().strip()
        valor = sair
        if sair in "SN":
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas a letra "S" ou "N".\033[m')
        if ok:
            break
    return valor

while True:
    dicionario["Nome"] = leianome("Nome: ")
    dicionario["Sexo"] = leiasexo("Sexo: [M]/[F]: ")
    dicionario["Idade"] = leiaidade("Idade: ")
    sair = leiasair("Deseja Continuar? [S][N]: ")

    cadastro.append(dicionario.copy())
    soma += dicionario["Idade"]
    media = soma / len(cadastro)

    if dicionario["Sexo"] == "F":
        mulheres.append(dicionario["Nome"])
    if sair == "N":
        break

print("-=" * 30)
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
print(f'B) O valor total da média do grupo é {media:.2f}')
print(f'C) O nome das mulheres cadastradas foram ', end="")
for n in mulheres:
    print(f'{n}; ', end="")
print()
print(f'D) Lista das pessoas que estão acima da média da idade:')
for i in range(0, len(cadastro)):
    if cadastro[i]["Idade"] > media:
        dict(cadastro[i])
        for k, v in cadastro[i].items():
            print(f'{k} = {v} ', end=";")
    print()
