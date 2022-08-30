"""34) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

s = float(input('Digite seu salario: '))

if s <= 1250:
    print(f'Com o aumento de 15% seu salário passa a ser R$ {s + (s * 0.15):.2f}')
else:
    print(f'Com o aumento de 10% seu salário passa a ser R$ {s + (s * 0.1):.2f}')