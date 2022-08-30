"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

c = 0

while c < 1:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('-='*5,'Menu','-='*5)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('Digite uma opção: '))
    print('-=' * 15)

    if opcao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        print('-=' * 15)
    elif opcao == 2:
        print(f'{n1} X {n2} = {n1*n2}')
        print('-=' * 15)
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior numero é {n1}.')
            print('-=' * 15)
        else:
            print(f'O maior numero é {n2}.')
            print('-=' * 15)
    elif opcao == 5:
        c += 1
print('Obrigado por usar nosso programa!')
