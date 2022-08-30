"""77) Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

nomes = ('Luiz', 'Counter', 'Strike', 'Fallen', 'Fenix', 'Fernando', 'Boltz', 'Vinicius')

for palavras in nomes:
    print(f'\nNa palavra {palavras} temos ', end='')
    for letra in palavras:
        if letra in 'aeiou':
            print(letra, end=' ')
