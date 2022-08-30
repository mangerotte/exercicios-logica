"""103) Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome, gols):
    if nome == "":
        nome = "<desconhecido>"
    if not gols.isnumeric():
        gols = 0
    else:
        int(gols)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = input('Nome do jogador: ')
g = input("Número de Gols: ")
ficha(jogador, g)