from random import randint

"""100) Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

numeros = []

def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(0,10))
    return print(lst)


def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c

    print(f"A soma dos pares é igual {soma}")




sorteia(numeros)
somaPar(numeros)
