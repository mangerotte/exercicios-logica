from datetime import date

"""39) Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

nascimento = int(input('Digite o ano de nascimento: '))
data_atual = date.today()
idade = data_atual.year - nascimento

if idade > 18:
    print(f'Você já se alistou! E já se passaram {idade-18} anos')
elif idade < 18:
    print(f'Você não está com idade o suficiente para se alistar! Ainda faltam {18-idade} anos')
else:
    print('Você deverá se alistar este ano!')