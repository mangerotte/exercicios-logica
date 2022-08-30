from datetime import date

"""101) Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

def voto(ano):
    idade = date.today().year - ano
    if 16 <= idade < 18 or idade >= 70:
        return print("VOTO OPCIONAL")
    elif idade > 18:
        return print("VOTO OBRIGATÓRIO!")
    else:
        return print("VOTO NEGADO")




voto(int(input("Digite o ano de nascimento: ")))