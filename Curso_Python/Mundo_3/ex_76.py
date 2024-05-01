print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # Aqui centraliza
print("-" * 40)
listagem = ('Lapis', '1.75',
            'Borracha', '2.00',
            'Carderno', '15.90',
            'Estojo', '25.00',
            'Transferidor', '4.20',
            'Compasso', '9.99',
            'Mochila', '120.32',
            'Canetas', '22.30',
            'Livro', '34.90')
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end='')  # aqui colca a direita
    else:
        print(f'{listagem[produto]:.>7}')  # aqui colca a esquerda
print("-" * 40)
