"""49) Refaça o DESAFIO 9,
mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

n = int(input('Digite o numero o qual você deseja saber a tabuada: '))

for x in range(0,10):
    multiplicacao = x * n
    print(f'{n} x {x} = {multiplicacao}')