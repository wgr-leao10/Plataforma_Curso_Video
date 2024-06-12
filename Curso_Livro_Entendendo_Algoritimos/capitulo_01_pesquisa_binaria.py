def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Posição do Elemento", pesquisa_binaria(minha_lista, 3))
print("Posição do Elemento", pesquisa_binaria(minha_lista, -1))
print("Posição do Elemento", pesquisa_binaria(minha_lista, 5))
