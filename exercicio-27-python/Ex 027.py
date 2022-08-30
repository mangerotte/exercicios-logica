"""27) Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

nome = input('Digite seu nome completo: ')
x = nome.split()
print(f'Primeiro nome = {x[0]}\nUltimo nome = {x[-1]}')