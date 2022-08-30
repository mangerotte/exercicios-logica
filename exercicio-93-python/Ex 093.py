"""93) Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato."""

jogador = {}
gols = []
total = 0
jogador["Nome"] = input('Digite o nome do jogador: ')
p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for g in range(1, p+1):
    gols.append(int(input(f'Quantos gols na partida {g}? ')))
jogador["Gols"] = gols
jogador["Total"] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for p, g in enumerate(jogador["Gols"]):
    print(f'=> Na partida {p+1}, fez {g} gols.')


