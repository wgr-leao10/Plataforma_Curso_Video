# apartir do python 3 não precisa de parentêses
# tuplas são imutáveis e heterogênias lanche[1] = "refrigerante"-comando errado
# Exemplo de tupla
lanche = ("Hamburger", "Suco", "Pizza", "Pudim", "Batata Frita")
print(lanche)
print(sorted(lanche))  # Aqui ele coloca em ordem alfabética

# Usando estrutura de repetição for
# Técnica 1

for comida in lanche:
    print(f"Eu vou comer Comida {comida}")

# Técnica 2

for cont in range(0, len(lanche)):
    print("Eu vou comer para caramba", lanche[cont])  # Lanche na posição cont

# Técnica 3, nesta da para mostrar a posição, como exemplo abaixo:

for cont in range(0, len(lanche)):
    print(f"Eu vou comer para caramba {lanche[cont]}, na posição {cont}")

# Técnica 4, nesta da para mostrar a posição, usando outra técnica:

for pos, comida in enumerate(lanche):  # o enumerate ele numera os itens
    print(f"Eu comi para caramba {comida}, na posição {pos}")
