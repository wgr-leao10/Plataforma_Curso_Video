from random import randint
print("-" * 40)
print(f'{"Jogo de Dados EX_91":^40}')
print("-" * 40)
sorteio = (randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4))
jogadores = {'Jogador1': 'Sorteio', 'Jogador2': 'Sorteio', 'Jogador3': "Sorteio", "Jogador4": "Sorteio"
}
print("RANKING DE JOGADORES")
print("-" * 40)
for i, j in jogadores.items():
    print(f"{i} tirou {sorteio}")
print("-" * 40)
