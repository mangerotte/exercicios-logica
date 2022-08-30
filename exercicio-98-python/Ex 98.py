"""98) Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

def contador(i, f, p):
    if p < 0 and i < 0:
        p *= -1
    if p == 0:
        if i > f:
            p = -1
        else:
            p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if i < f:
        for x in range(i, f+1, p):
            print(x, end=" ")
    elif i > f:
        for x in range(i, f-1, p):
            print(x, end=" ")
    print()
    print("-=" * 30)


contador(1, 10, 1)
contador(10, 0, -2)
print("Agora é sua vez de personalizar a contagem: ")
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))
