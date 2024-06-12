def pesquisa_binaria(lista, item):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            final = meio - 1
        else:
            inicio = meio + 1
    return None


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Posição do Elemento", pesquisa_binaria(minha_lista, 3))
print("Posição do Elemento", pesquisa_binaria(minha_lista, 5))
#  como colocar um input aqui na função