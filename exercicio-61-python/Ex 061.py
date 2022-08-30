"""61) Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
acumulador = 0
pa = [pt, ]

while c <= 10:
    if c < 1:
        acumulador = pt + razao
        pa.append(acumulador)
    acumulador += razao
    pa.append(acumulador)
    c += 1
print(pa)