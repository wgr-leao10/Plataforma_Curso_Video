print("-" * 40)
print(f'{"Extraindo dados de uma lista EX_81":^40}')
print("-" * 40)
i = 0
cont_elementos = 0
numeros = list()
while i != "N":
    n = int(input("Digite um valor: "))
    numeros.append(n)
    cont_elementos += 1
    i = " "
    while i not in 'SN':
        i = str(input("Deseja Continuar[S/N]")).strip().upper()[0]
print("-" * 40)
numeros = sorted(numeros, reverse=True)
print(f"Você digitou {cont_elementos} elementos")
print(f"Os Valores em ordem descrecente {numeros}")
if 5 in numeros:
    print("O Valor 5 Faz Parte desta lista")
else:
    print("O valor 5 não fz parte desta lista")
