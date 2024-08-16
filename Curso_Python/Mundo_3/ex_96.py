def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Contole de terrenos Ex_96":^40}'))


def areaterreno(largura, altura):
    area = largura * altura
    print(f'A área de um terreno {largura} x {altura} é de {area}')


# programa principal
largura = float(input("Largura (m):"))
altura = float(input("Largura (m):"))
areaterreno(largura, altura)
