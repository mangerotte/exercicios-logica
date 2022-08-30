"""44) Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

produto = float(input('Digite o valor do produto: '))
pagamento = input('Dinheiro, Cheque, Cartão: ')

if pagamento == 'Cartão':
    parcela = input('A vista, 2x, 3x, ou mais: ')
    if parcela == 'A vista':
        valor = produto - (produto * 0.05)
        print(f'O produto custa R$ {produto:.2f} e com desconto de 5% sairá por R$ {valor:.2f}.')
    elif parcela == '2x':
        print(f'O produto sairá por R$ {produto:.2f}, não haverá desconto.')
    else:
        valor = produto + (produto + (produto * 0.2))
        print(f'O custa R$ {produto:.2f} sairá por R$ {valor:.2f}')
else:
    valor = produto - (produto * 0.1)
    print(f'O produto custa R$ {produto:.2f} e com desconto sairá por R$ {valor:.2f}')
