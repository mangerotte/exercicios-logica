"""62) Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
acumulador = 0
pa = [pt, ]
v = 0

while c <= 7:
    if c < 1:
        acumulador = pt + razao
        pa.append(acumulador)
    acumulador += razao
    pa.append(acumulador)
    c += 1

print(pa)
print('''Você deseja mostrar mais algum termo?
    [1] Sim
    [2] Não''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    termo = int(input('Quantos mais termos deseja ver: '))
    while v < termo:
        acumulador += razao
        v += 1

else:
    print('Obrigado! Volte sempre!')




