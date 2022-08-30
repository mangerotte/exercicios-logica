"""73) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

time = ('Corinthians', 'Bragantino', 'Atletico-MG', 'Coritiba', 'São Paulo',
        'Santos', 'Cuiabá', 'Internacional', 'Avaí', 'America-MG',
        'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará'
        'Athletico-PR', 'Atletico-GO', 'Goias', 'Juventude', 'Fortaleza')
print('-='*20)
print('OS PRIMEIROS 5 TIMES!')
print('-='*20)
print(time[:5])
print('-='*20)
print('OS ÚLTIMOS 4 COLOCADOS')
print('-='*20)
print(time[-4:])
print('-='*20)
print('TIMES EM ORDEM ALFABETICA')
print('-='*20)
print(sorted(time))
print('-='*20)
print('POSIÇÃO ATLETICO-MG')
print('-='*20)
print(f'O Atletico-MG está na posição {time.index("Atletico-MG")+ 1}º')
