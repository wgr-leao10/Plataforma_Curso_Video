from random import randint


def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Funções Sortear e Somar Ex_100":^40}'))


def sorteio(list):
    for cont in range(0, 5):
        list.append(randint(1, 10))


def somapar(list):
    soma = 0
    for v in list:
        if v % 2 == 0:
            soma += v
        print(f'Soma dos numeros pares da {list}, temos {soma}')


#  parte principal
numeros = list()
sorteio(numeros)
print(numeros)
somapar(numeros)