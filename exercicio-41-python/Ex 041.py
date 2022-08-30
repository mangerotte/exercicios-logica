from datetime import date

"""41) A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
data_atual = date.today()
idade = data_atual.year - ano_nascimento

if idade < 9:
    print('Mirim')
elif 9 < idade < 14:
    print('Infatil')
elif 14 < idade < 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')


