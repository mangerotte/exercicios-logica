"""97) Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~"""

def escreva(msg):
    c = len(msg)
    print("~"*c)
    print(msg)
    print("~"*c)


escreva("Olá Mundo")
escreva("CE TA DOIDOOOOOOOOOOOOOOOOOOOOOOOOO")