def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Função Para Fotorial Ex_102":^40}'))


def fatorial(num, show=False):
    """
    Está função retorna o fatorial de um número.
    Os Parâmetros:
    Primeiro Prametro (num): O número a ser calculado
    Segundo  Prametro (Show): Ele é opcional,
    caso escolhido apresenta o detalhe da soma
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print('x', end="")
            else:
                print('=', end="")
        f *= c
    return f


#  Programa Principal
print(fatorial(5, show=True))
help(fatorial)