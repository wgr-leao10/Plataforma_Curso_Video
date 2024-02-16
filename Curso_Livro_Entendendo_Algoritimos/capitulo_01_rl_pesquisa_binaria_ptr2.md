## Relatório do Código
 A descrição e a explicação completa esta na pagina 26 e 27 do livro, mas a funcão pesquisa binária funciona assim:

1. `minha_lista = [1, 3, 5, 7, 9]`: Aqui, estamos criando uma lista chamada `minha_lista` que contém os elementos `[1, 3, 5, 7, 9]`. Esta lista está ordenada em ordem crescente.

2. `print("Posição do elemento 3:", pesquisa_binaria(minha_lista, 3))`: Esta linha imprime a posição do elemento 3 na lista `minha_lista`. Para fazer isso, chamamos a função `pesquisa_binaria` passando `minha_lista` como o primeiro argumento e o valor 3 como o segundo argumento. A função `pesquisa_binaria` retorna a posição do elemento 3 na lista, se estiver presente, ou `None` se o elemento não estiver na lista. Esta posição é então impressa na saída padrão junto com a mensagem "Posição do elemento 3:".

3. `print("Posição do elemento -1:", pesquisa_binaria(minha_lista, -1))`: Da mesma forma, esta linha imprime a posição do elemento -1 na lista `minha_lista`. Novamente, chamamos a função `pesquisa_binaria` passando `minha_lista` como o primeiro argumento e o valor -1 como o segundo argumento. A função retorna a posição do elemento -1 na lista, se estiver presente, ou `None` se o elemento não estiver na lista. Esta posição é então impressa na saída padrão junto com a mensagem "Posição do elemento -1:".

Em resumo, essas linhas de código demonstram como usar a função `pesquisa_binaria` para encontrar a posição de elementos específicos em uma lista ordenada.

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    chute = int(input("Escola um número e veja sua posição: "))
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
print(f"Pesquisa Binária {chute}")
