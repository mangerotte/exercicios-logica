import random

"""58) Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer."""

acerto = 0
palpite = 0

while acerto < 1:
    n = int(input('Digite um numero: '))
    s = random.randint(0, 5)
    if n == s:
        print(f'Você acertou o numero que o PC escolheu foi {s}')
        acerto += 1
    else:
        print(f'Você errou! O numero que o PC escolheu foi {s}')
        palpite += 1
print(f'Você teve que dar {palpite} palpites para acertar o número!')