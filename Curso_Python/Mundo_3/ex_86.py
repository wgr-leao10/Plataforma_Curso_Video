print("-" * 40)
print(f'{"Matrizes em Python EX_86":^40}')
print("-" * 40)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):  # Aqui pega a linha
    for j in range(0, 3):  # Aqui pega a coluna
        matriz[i][j] = int(input(f"Digite um valor para {[i]}{[j]}: "))
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:5^}]", end=' ')
    print()
print("-" * 40)
