soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f"Digite Número {i}: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Os nímeros pares são {cont}, e sua soma dos Números é igual {soma}")
