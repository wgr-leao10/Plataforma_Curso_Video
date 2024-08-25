#  help(print) - Forma mais comum de acessar a dicstring

# print(input.__doc__)

# docstring aqui um exemplo básico
x = 10
# Variárial global


def somar(a, b, c=0):
    """
    Está função retorna a soma de até três números.
    Se o terceiro número não for fornecido, ele assume o valor 0, pois é um
    parâmetro opcional
    Os Parâmetros:
    a (int ou  float): Primeiro Número
    b (int ou  float): Segundo Número
    c (int ou  float): Terceiro Número, parametro opcional, por padrão é 0

    """
    #  Variável local
    s = a + b + c
    print(s)


help(somar)
#  Aqui é a consulta da função somar()
