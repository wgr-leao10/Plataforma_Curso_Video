print("-" * 40)
print(f'{"Matrizes em Python Com Analise de Dados EX_87":^40}')
print("-" * 40)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior_valor = soma_coluna = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para {[i]}{[j]}: "))
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:5^}]", end=' ')
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
    print()
for i in range(0, 3):
    soma_coluna += matriz[i][2]
for j in range(0, 3):
    if j == 0:
        maior_valor = matriz[i][j]
    elif matriz[i][j] > maior_valor:
        maior_valor = matriz[i][j]
print("-" * 40)
print(f"A soma dos Valores pares são {soma_pares}")
print(f"A soma dos Valores da terceira coluna é {soma_coluna}")
print(f"O maior Valor da Segunda linha é {maior_valor}")
print("-" * 40)
