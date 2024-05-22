print("-" * 40)
print(f'{"Dividindo os valores em várias Listas EX_82":^40}')
print("-" * 40)
numeros = list()
numeros_par = list()
numeros_impar = list()
i = 0
while i != "N":
    n = int(input("Digite Um Número: "))
    numeros.append(n)
    i = " "
    while i not in 'SN':
        i = str(input("Deseja Continuar [S/N]")).strip().upper()[0]
    if n % 2 == 0:
        numeros_par.append(n)
    else:
        numeros_impar.append(n)
print("-" * 40)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numeros_par}')
print(f'A lista de impar é {numeros_impar}')
