"""31) Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

d = int(input('Digite a distância da viagem: '))

if d < 200:
    print(f'A passagem irá custar R${d*0.50}')
else:
    print(f'A passagem irá custar R${d * 0.45}')