# ve qual é o nome do jogadar e a quantidade de partidas
jogo = {'nomes':  input('qual é o seu nome: ')}
print('''.
.''')
partidas = int(input('quantas partidas vc jogou?? '))
print('''.
.''')
gol = []
oiee = 0
for quantidade in range(partidas):
    gol.append(int(input(f'vc fez quantos gols na {quantidade + 1}: ')))
print('.')
# ve quantos gols o jogador fez em cada partida
for g in gol:
    oiee += g
jogo['g'] = oiee
jogo['partidas'] = partidas
# mostrar para o usuario o resultado
print(f'''o nome do jogador(a): {jogo['nomes']}
----------------------------------------------
a quantidades de partidas jogadas foi: {jogo['partidas']}
----------------------------------------------
a quantidades de gol no compeonato é: {jogo['g']}''')