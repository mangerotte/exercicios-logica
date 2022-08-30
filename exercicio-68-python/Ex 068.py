import random

"""68) Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""


v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = input('Escolha PAR ou ÍMPAR: ').upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogador novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')