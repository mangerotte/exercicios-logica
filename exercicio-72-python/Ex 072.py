"""72) Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

tupla = (
'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = ' '
    sair = ' '
    while n not in range(0, 21):
        n = int(input('Digite um numero: '))
    while sair not in 'SsNn':
        sair = input('Deseja Continuar? [S]im [N]ão: ').strip().upper()[0]

    if sair == 'N':
        print('Obrigado por usar nosso programa!')
        break

    print(tupla[n])
