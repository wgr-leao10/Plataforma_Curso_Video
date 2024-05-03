num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # acrescentar item
num.sort()  # ordenar item
num = sorted(num)  # ordenar os itens semelahnate a sort
num = sorted(num, key=len)  # ordena os itens apartir do tamanho da string
num = sorted(num, reverse=True)  # ordena os itens de modo descresente
num = sorted(num, key=lambda)  # aqui ordena em ordem inversa a lista de string
num.sort(reverse=True)  # reverter a ordem
num.insert(2, 0)  # aqui é para inserir, se lê inserir item 0 na posição 2
num.pop()  # aqui deleta o ultimo elemento da lista
num.pop(2)  # aqui deleta o iem na posição 2
num.remove(2)  # semelhante ao anterior remove o item na índece 2
if 8 in num:  # Aqui verifica se existe o índice
    num.remove(8)  # se for vrdadeiro ele remove
else:
    print("nÃO ACHEI O 8")
print(num)
print(f'Esta lista tem {len(num)} itens')
