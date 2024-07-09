print("-" * 40)
print(f'{"Cadastro de Joagador De Futebol EX_93":^40}')
print("-" * 40)
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador?:  '))
total = int(input(f"Quantas Partidas {jogador["nome"]} jogou?  "))
for i in range(0, total):
    partidas.append(int(input(f'Quantas gols na partida {i}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print("=-=" * 40)
print(jogador)
print("=-=" * 40)
for i, j in jogador.items():
    print(f'O campo {i} tem valor {j}')
print("=-=" * 40)
print(f' O jogador {jogador["nome"]} jogou {total} Partidas')
for k, v in enumerate(jogador["gols"]):
    print(f'   => Na Partida {k}, fez {v} gols.')
print(f'Foi um Total de {jogador["total"]} gols.')
