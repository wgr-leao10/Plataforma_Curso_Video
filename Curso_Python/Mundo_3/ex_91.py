from random import randint
from operator import itemgetter  # Aqui para ordenar descresente
print("-" * 40)
print(f'{"Jogo de Dados EX_91":^40}')
print("-" * 40)
sorteio = (randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4))
jogadores = {'Jogador1': 'Sorteio', 'Jogador2': 'Sorteio', 'Jogador3': "Sorteio", "Jogador4": "Sorteio"
}
print("RANKING DE JOGADORES")
jogadores = {'Jogador1': randint(0, 6),
             'Jogador2': randint(0, 6),
             'Jogador3': randint(0, 6),
             "Jogador4": randint(0, 6)}
ranking = list()
print("Valores Sorteados")
print("-" * 40)
for i, j in jogadores.items():
    print(f"{i} tirou {sorteio}")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado")
print("-" * 40)
print("== RANKING DE JOGADORES==")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# Aqui para ordenar descrescente
#  ranking = dict(sorted(joagdore.items(), key=lambda item[1], reverse=True))
for i, j in enumerate(ranking):
    print(f"{i+1}° lugar: {j[0]} com {j[1]}")
print("-" * 40)
