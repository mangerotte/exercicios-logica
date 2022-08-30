"""53) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
frase_invertida = ''

for letra in range(len(junto) -1, -1, -1):
    frase_invertida += junto[letra]

if frase_invertida == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')