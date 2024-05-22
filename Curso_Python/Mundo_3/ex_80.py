print("-" * 40)
print(f'{"LISTA ORDENADA SEM REPETICOA EX_80":^40}')
print("-" * 40)
lista = []
for c in range(0, 5):
    n = int(input("Digite Um Valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista(pos):
                lista.insert(pos, n)
                break
            pos += 1
print("-" * 40)
print(f'Os Valores digitados em ordem foram {lista}')
