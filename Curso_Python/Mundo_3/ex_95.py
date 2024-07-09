print("-" * 40)
print(f'{"Aprimorando Dicionário EX_95":^40}')
print("-" * 40)
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador?:  '))
    total = int(input(f"Quantas Partidas {jogador["nome"]} jogou?  "))
    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'Quantas gols na partida {i}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = input('Deseja continuar[S/N]?: ').strip().upper()[0]
        if resposta in ('S', 'N'):
            break
        print('ERRO! Digite apenas S ou N')
    if resposta == 'N':
        break
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15} ', end=' ')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15} ', end=' ')
    print()
print("-" * 40)
while True:
    opcao = int(input("Mostrar dados de qual Jogador(999 para parar)?: "))
    if opcao == 999:
        break
    if opcao >= len(time):
        print(f'ERRO!: Código {opcao} de jogador Não existe')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[opcao]["nome"]}:')
        for i, g in enumerate(time[opcao]['gols']):
            print(f' no jogo {i+1} fez {g} gols')
    print("-" * 40)
print('VOLTE SEMPRE...')
