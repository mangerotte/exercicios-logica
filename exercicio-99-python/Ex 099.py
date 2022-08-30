from random import randint

"""99) Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

def maior(*args):
    m = 0
    print("Analisando os valores passados ...")
    print(*args, end=" ")
    print(f'Foram passados {len(args)} valores ao todo.')
    for c in args:
        if c == 0:
            m = c
        if c > m:
            m = c
    print(f'O maior número informado é {m}')
    print("-="*30)


maior(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10))
maior(randint(0,10))
maior()