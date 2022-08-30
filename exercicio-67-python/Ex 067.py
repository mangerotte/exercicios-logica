"""67) Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    n = int(input('Digite qual número deseja saber a tabuada: '))
    print('-=' * 20)
    for c in range(0, 11):
        resultado = c * n
        print(f'{n} X {c} = {resultado}')
    print('-='*20)
    print(('Deseja sair? [1] Sim [2] Não'))
    flag = int(input('Digite a opção: '))
    if flag == 1:
        break
print('-='*20)
print('Obrigado por usar nossa Tabuada!')