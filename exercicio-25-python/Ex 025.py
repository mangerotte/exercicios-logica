"""25) Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""


n = input('Digite seu nome completo: ')
silva = "Silva" in n

if silva == True:
    print('Possui o nome "Silva" no nome')
else:
    print('Não possui "Silva" no nome')