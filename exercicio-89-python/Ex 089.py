"""89) Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o
usuário possa mostrar as notas de cada aluno individualmente."""

lista = []
temp = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    sair = input('Deseja continuar? [S]im ou [N]ão: ').upper().strip()
    temp.append(nome), temp.append(n1), temp.append(n2)
    lista.append(temp[:])
    temp.clear()
    if sair == 'N':
        break
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"Média":>10}')
print('-'*30)
for i in range(0, len(lista)):
    print(f'{i:<4} {lista[i][0]:<10} {((lista[i][1]+lista[i][2])/2):>8.1f}')
print('-'*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]}')
    if aluno == 999:
        break
