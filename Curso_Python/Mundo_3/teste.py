lanche = ("Hamburger", "Suco", "Pizza", "Pudim", "Batata Frita")

for cont in range(0, len(lanche)):
    print("Eu vou comer para caramba", lanche[cont])  # Lanche na posição cont

# Técnica 3, nesta da para mostrar a posição, como exemplo abaixo:

for cont in range(0, len(lanche)):
    print(f"Eu vou comer para caramba {lanche[cont]}, na posição {cont}")

# Técnica 4, nesta da para mostrar a posição, usando outra técnica:

for pos, comida in enumerate(lanche):  # o enumerate ele numera os itens
    print(f"Eu comi para caramba {comida}, na posição {pos}")

