# Uma caracteristica do python seria a ligação de lista
# quando muda um item muda na que esta ligada
# veja o exemplo
a = [2, 3, 4, 7]
# b = a  # aqui é uma ligação de a e b
b = a[:]  # Aqui foi feito uma cópia de a em b ai nao tem mais ligação
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
