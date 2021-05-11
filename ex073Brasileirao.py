'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
#2020
brasileirao = 'Flamengo','Internacional', 'Atlético - Mg', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athlético - PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético - GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'
print('{:=^40}'.format('TABELA BRASILEIRÃO'))
print(brasileirao)
print('{:=^40}'.format('POSIÇÃO DO BRAGANTINO'))
print(brasileirao.index('Bragantino'))
print('{:=^40}'.format('LIBERTADORES'))
print(brasileirao[0:5])
print('{:=^40}'.format('LANTERNAS'))
print(brasileirao[16:])
print('{:=^40}'.format('ORDEM ALFABÉTICA'))
print(sorted(brasileirao))