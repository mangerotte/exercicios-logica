"""104) Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)"""

def leiaint(n):
    active = True
    while active:
        if not n.isnumeric():
            print("Digite apenas números!")
            n = input("Digite um número: ")
        else:
            int(n)
            active = False
    return n

numero = leiaint(input("Digite um número: "))
print(numero)