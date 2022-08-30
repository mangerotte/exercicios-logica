"""81) Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente."""

lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = input('Deseja continuar? [S/N]: ').upper().strip()
    if r == 'N':
        print('Obrigado por usar nosso programa!')
        break
print('-='*30)
if 5 in lista:
        print('Existe o valor 5 na lista!')
else:
    print('Não existe o valor 5 na lista')
print(f'Foram digitados {len(lista)} elementos.')
print(f'A lista de valores ordenadas de forma decrescente é {sorted(lista, reverse=True)}')