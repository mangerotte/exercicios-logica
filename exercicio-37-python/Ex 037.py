"""37) Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal."""

n = int(input('Digite um numero: '))
o = int(input('Escolha a opção:\n[1] Binario \n[2] Octal\n[3] Hexadecimanl\n'))


if o == 1:
    binary = bin(n)
    print(binary[2:])
elif o == 2:
    octal = oct(n)
    print(octal[2:])
elif o == 3:
    hexa = hex(n)
    print(hexa[2:])
else:
    print('Digite um numero valido!')
