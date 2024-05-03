print("-" * 40)
print(f'{"ANALISANDO NÙMEROS EX_78":^40}')
print("-" * 40)
numeros = []
maior = 0
menor = 0
for i in range(0, 5):
    numeros.append(int(input(f'Você digitou na para a posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print(f'Você digitou os valores{numeros}')
print(f'O maior Valor digitado {max(numeros)}, nas posiçoes {i}...{i}')
print(f'O menor Valor digitado {min(numeros)}, nas posições {i}')
print(f'O maior Valor digitado {maior}, nas posições', end=' ')
for j, c in enumerate(numeros):
    if c == maior:
        print(f"{j}...", end=' ')
print()
print(f'O menor Valor digitado {menor}, nas posições', end=' ')
for j, c in enumerate(numeros):
    if c == menor:
        print(f"{j}...", end=' ')
print()
print("-" * 40)
