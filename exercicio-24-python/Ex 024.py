"""24) Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

cidade = input('Digite o nome da sua cidade: ')
prefixo = cidade.startswith('Santo')

if prefixo == False:
    print('Sua cidade não começa com a palavra "Santo"')
else:
    print('Sua cidade começa com a palavra "Santo"')