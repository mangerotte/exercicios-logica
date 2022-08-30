import random

"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

alunos = ['Luiz', 'Ana', 'Cecilia', 'Eduarda']
lista = [1, 2, 3, 4, 5, 6]

random.shuffle(alunos)

print(f'O aluno selecionado foi {random.choice(alunos)}')
print(f'A ordem das apresentações será de primeiro {alunos} ')