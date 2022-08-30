"""82) Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    r = input('Deseja continuar: [S/N]').upper().strip()
    if r == 'N':
        break
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista com todos elementos é {lista}')
print(f'A lista com somente números pares é {par}')
print(f'A lista com somente números ímpares é {impar}')