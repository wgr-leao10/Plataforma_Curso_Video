def titulo(txt):
    tam = len(txt) + 4
    print("-" * tam)
    print(f'  {txt}')
    print("-" * tam)


titulo((f'{"Um print Especial Ex_97"}'))


def escreva(texto):
    tam = len(texto) + 4
    print("-" * tam)
    print(f'  {texto}')
    print("-" * tam)


#  Programa Prncipal
Mensagem = input("Escreva o Título: ")
escreva(Mensagem)
