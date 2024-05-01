print("-" * 40)
print(f'{"ANALISANDO NÙMEROS EX_78":^40}')
print("-" * 40)
numeros = []
for i in range(0, 5):
    numeros.append(int(input(f'Você digitou na para a posição {i}: ')))
print(f'Você digitou os valores{numeros}')
print(f'O maior Valor digitado {max(numeros)}, nas posiçoes {i}...{i}')
print(f'O menor Valor digitado {min(numeros)}, nas posições {i}')
print("-" * 40)
