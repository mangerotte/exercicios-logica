from random import randint
from operator import itemgetter

"""91) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

jogo = {}
ranking = []
jogo['Jogador 1'] = randint(1, 6)
jogo['Jogador 2'] = randint(1,6)
jogo['Jogador 3'] = randint(1,6)
jogo['Jogador 4'] = randint(1,6)
for k, v in jogo.items():
    print(f'O {k} tirou {v} nos dados')
print("-="*30)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k, i in enumerate(ranking):
    print(f'{k+1}º lugar = {i[0]} que tirou {i[1]} nos dados ')