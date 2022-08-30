"""22) Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""


nome = 'Luiz Augusto Mangerotte Andrade'

print(nome.upper())
print(nome.lower())
lista = nome.split()
se = ''.join(lista)
print(len(se))
print(len(lista[0]))