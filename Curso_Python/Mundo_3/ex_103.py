def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Ficha Jogador Ex_103":^40}'))


def ficha(nome='', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


# Programa Principal
nome = input("Nome do Jogador: ").strip()
gols = input("Número de Gols: ").strip()

# Verificar se nome é vazio
if nome == "":
    nome = "Nome desconhecido"

# Verificar e tratar a entrada de gols aqui confirma se é numero
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0  # Se não for número, assume 0 gols

ficha(nome, gols)
