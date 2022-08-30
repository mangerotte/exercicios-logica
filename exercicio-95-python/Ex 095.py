"""95) Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

time = {}
gols = []
lista_time = []


def validadornome(msg):
    ok = False
    while True:
        nome = input(msg)
        if not nome.isdigit():
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas letras.\033[m')
        if ok:
            break
    return nome


def validadorint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas números.\033[m')
        if ok:
            break
    return valor


def validadorsaida(msg):
    ok = False
    while True:
        saida = input(msg).upper().strip()
        if saida in "SN":
            ok = True
        else:
            print('\033[0;31mERRO! Digite apenas "S" ou "N".\033[m')
        if ok:
            break
    return saida


while True:

    time["Jogador"] = validadornome("Nome do jogador: ")
    time["Partidas"] = validadorint(f'Digite quantas partidas o {time["Jogador"]} jogou: ')

    for p in range(0, time["Partidas"]):
        gols.append(validadorint(f"Quantos gols na {p+1} partida? "))

    time["Gols"] = gols[:]
    time["Total"] = sum(gols)
    lista_time.append(time.copy())
    gols.clear()

    sair = validadorsaida("Deseja Continuar? [S] ou [N]: ")
    if sair == "N":
        break

print("-="*30)
print(f'{"Cod.":<10}{"NOME":<10}{"Partidas":<10}{"Gols":>11}{"Total":>11}')
print("--"*30)
for i, v in enumerate(lista_time):
    print(f'{str(i):<10}', end='')
    for p in lista_time[i].values():
        print(f'{str(p):<13}', end="")
    print()
print("--"*30)
while True:

    while True:
        cod = validadorint("Escolha o codigo do jogador para carregar os dados: (999 para parar): ")
        if cod >= len(lista_time) and cod != 999:
            print("\033[0;31mERRO! Digite um valor válido.\033[m")
        else:
            break

    if cod == 999:
        break

    print(f'- Levantamento dos dados do jogador {lista_time[cod]["Jogador"]}: ')

    for i, p in enumerate(lista_time[cod]["Gols"]):
        print(f'Na partida {i+1}, {lista_time[cod]["Jogador"]} fez {p} gols. ')

    print("--" * 30)