def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo("Função Soma")


def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")


soma(10, 6)


def contador(*num):  # Aqui seria a o desempacotamento
    tam = len(num)
    for valor in num:
        print(f'{valor}', end="-")
    print(f'Recebi os valores e são ao todo {tam} números')


contador(1, 2, 3, 4)
contador(3, 5, 9)
contador(1, 2, 90, 12, 25, 36, 45)


def dobra(lista):  # usando lista
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 3, 4, 5, 6]
dobra(valores)
print(valores)


def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} temos {s}')


soma2(1, 2, 3, 4)
soma2(3, 5, 9)
soma2(1, 2, 90, 12, 25, 36, 45)