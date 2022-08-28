active = True
s = 0

while active:

    n = int(input('Digite um numero: '))

    if n == 1111:
        break

    s = n + s

print(f'A soma total dos numeros digitado foi de {s}')