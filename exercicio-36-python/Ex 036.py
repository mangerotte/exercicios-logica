"""36) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

c = float(input('Valor da casa: '))
s = float(input('Valor do salário: '))
t = int(input('Quanto tempo deseja pagar em meses o empréstimo: '))

parcela = c / t
porcentagem = s * 0.3

if porcentagem > parcela:
    print(f'O seu empréstimo foi aprovado! A prestação irá ser de R$ {parcela:.2f} e 30% do seu salário é R$ {porcentagem:.2f}')
else:
    print(f'Empréstimo negado! A prestação írá ser de R$ {parcela:.2f}! A parcela maxima tem que ser R$ {porcentagem:.2f}')