"""75) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

tupla = []
par = 0
for c in range(0,5):
    n = int(input('Digite um número: '))
    tupla.append(n)
    if n % 2 == 0:
        par += 1

tupla = tuple(tupla)

print(f'''O número 9 apareceu {tupla.count(9)} vezes;
O número 3 apareceu no {tupla.index(3)}º indice;
Apareceram {par} números pares.''')