"""70) Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:"""

total = 0
produto_mil = 0
produto_barato = 0
nome_barato = ' '
c = 0
while True:
    produto = input('Digite o nome do produto: ')
    valor = ' '
    sair = ' '

    while not valor.isdigit():
        valor = input('Digite o valor do produto: ').replace('.', '')
    while not sair in 'SN':
        sair = input('Deseja continuar [S]im ou [N]ão: ').upper().strip()

    valor = int(valor)

    if c < 1:
        nome_barato = produto
        produto_barato = valor
        c += 1

    total += valor

    if valor > 1000:
        produto_mil += 1

    if valor < produto_barato:
        nome_barato = produto

    if sair == 'N':
        break
print(f'''O total gasto na compra foi R$ {total}
{produto_mil} valem mais de R$ 1000,00
O produto mais barato foi {nome_barato}''')