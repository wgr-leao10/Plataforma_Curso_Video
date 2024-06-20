print("-" * 40)
print(f'{"Lista com Pares e Impares EX_85":^40}')
print("-" * 40)
numeros = [[], []]
for i in range(0, 7):
for i in range(1, 8):
    n = int(input(f"Digite o {i}° valor: "))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
    numeros[0].sort()
    numeros[1].sort()
print(f"Os valores Pares Digitados foram {numeros[0]}")
print(f"Os Valores Impares digitados foram {numeros[1]}")
print("-" * 40)
