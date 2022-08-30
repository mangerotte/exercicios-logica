"""106) Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores."""

def sistema(nome):
    print("\033[0;31m~\033[m"*40)
    print(f"\033[0;31m  Acessando o Manual do comando {nome}\033[m")
    print("\033[0;31m~\033[m"*40)
    print(f'\033[0;31m{help(nome)}\033[m')



manual = input("Função ou Biblioteca > ")
sistema(manual)