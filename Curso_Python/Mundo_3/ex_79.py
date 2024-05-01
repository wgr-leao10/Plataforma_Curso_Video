print("-" * 40)
print(f'{"LISTA DE NÙMEROS EX_79":^40}')
print("-" * 40)
i = 0
numeros = list()
while i != 'N':
    n = int(input("Digite um Valor Para Ser Adionado: "))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado Com Sucesso...')
    else:
        print("Número Duplicado")
    i = " "
    while i not in 'SN':
        i = str(input("Deseja Continuar[S/N]")).strip().upper()[0]
print("-" * 40)
numeros.sort
print(f"Você Digitou os Números{numeros}")
