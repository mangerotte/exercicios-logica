"""65) Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

c = 1
maior = 0
menor = 0
soma = 0

while True:
    n = int(input('Digite um número inteiro: '))
    continuar = input('Deseja continuar: [S]im [N]ão: ').upper()
    if continuar == 'N':
        break
    if c <= 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    c += 1
media = soma / c
print(f'A média dos valores digitados foi de {media:.2f}, o maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
