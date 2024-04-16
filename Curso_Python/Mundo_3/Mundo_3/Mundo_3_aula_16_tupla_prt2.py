# Nete exemplo ele concatena as tuplas na ordem da soma
# se for a+ b será uma ordem para c e se for o opsto b + a o c fica diferente
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Aqui a ordem faz a diferença
print(c)
print(c.count(5))  # quantas vezes ocorre o número 5
print(c.index(8))  # qual o índice que número 8 apartir da primeira ocorrência
print(c.index(5, 1))  # Caso tenha + de uma ocorrência, colocar o deslocamento
