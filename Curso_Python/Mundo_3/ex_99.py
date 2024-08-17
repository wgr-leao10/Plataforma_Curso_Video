from time import sleep


def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Função que descobri o Maior EX_99":^40}'))


def maior(*num):
    cont = maior = 0
    print("\n Analisando os Valores Passados...")
    for valor in num:
        print(f'{valor}', end=" ", flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram Informados {cont} valores ao todo')
    print(f'O maior valor informado foi {valor}')    


#  programa principal
maior(3, 5, 9)
