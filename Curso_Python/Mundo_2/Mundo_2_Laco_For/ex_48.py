soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f"A soma dos {cont} valores solicitados é {soma}")
