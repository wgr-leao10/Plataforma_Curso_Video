def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{" Validando a entrada de Dados Ex_104":^40}'))


def leiaInt(prompt=""):
    while True:
        try:
            valor = int(input(prompt))
            return valor
        except ValueError:
            print("Por Favor, Digite um número inteiro Válido!")


#  programa principal
n = leiaInt('Digite um Número: ')
print(f'Você Acabou de digitar um número {n}')