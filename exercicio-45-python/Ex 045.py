import random

"""45) Crie um programa que faça o computador jogar Jokenpô com você"""

jogador = input('Escolha entre Pedra, Papel e Tesoura: ')

pc = ['Pedra', 'Papel', 'Tesoura']

sorteio = random.choice(pc)

if jogador == 'Pedra' and sorteio == 'Tesoura' or jogador == 'Papel' and sorteio == 'Pedra' or jogador == 'Tesoura' and sorteio == 'Papel':
    print(f'Você ganhou! Você escolheu {jogador} e o computador escolheu {sorteio}')

elif jogador == sorteio:
    print(f'Empate! Você escolheu {jogador} e o computador escolheu {sorteio}')

else:
    print(f'Você perdeu! Você escolheu {jogador} e o computador escolheu {sorteio}')
