print("-" * 40)
print(f'{"LISTA ORDENADA SEM REPETICOA EX_80":^40}')
print("-" * 40)
numeros = list()
while i != 'N':
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Número Duplicado..')
    i = " "
    while i not in 'SN':
        i = str(input("Deseja continuar[S/N]")).strip().upper()[0]
numeros = sorted(numeros)
print(f'Os numeros que vc digitou{numeros}')
print("-" * 40)
# corrigir o final