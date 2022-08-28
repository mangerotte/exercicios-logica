active = True
s = 0

while active:
    n = int(input('Digite um numero: '))
    s = n + s

    if n == 1111:
        active = False

print(f'A soma total dos numeros digitado foi de {s}')