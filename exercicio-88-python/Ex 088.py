import time
from random import randint

"""88) Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta."""

qts_sorteio = int(input('Digite o valor de quantos sorteios você deseja: '))
lista = []
temp = []
for c in range(0, qts_sorteio):
    for n in range(0, 6):
        temp.append(randint(0,60))
    lista.append(temp[:])
    temp.clear()
print('-='*5, "SORTEIO MEGA SENA", '=-'*5)
for x in range(len(lista)):
    print(f'Jogo {x+1}: {lista[x]}')
    time.sleep(1)
print('-='*6, "< BOM JOGO >", '=-'*6)