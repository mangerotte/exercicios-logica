import math

"""18) Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

angulo = float(input("Digite o ângulo que deseja: "))
radiano = math.radians(angulo)

seno = math.sin(radiano)
print(f'O seno de {angulo}º é de {seno:.2f}')
cosseno = math.cos(radiano)
print(f'O cosseno de {angulo}º é de {cosseno:.2f}')
tangente = math.tan(radiano)
print(f'A tangente de {angulo}º é de {tangente:.2f}')
