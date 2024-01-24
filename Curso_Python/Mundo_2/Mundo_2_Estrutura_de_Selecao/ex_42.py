print('--' * 20)
print('Analisador de Triangulo')
print('--' * 20)
n1 = int(input('Primeiro Seguimento: '))
n2 = int(input('Segundo Seguimento: '))
n3 = int(input('Terceiro Seguimento: '))
if n3 < n1 + n2 and n2 < n1 + n3 and n1 < n2 + n3:
    if n1 == n2 == n3:
        print('Os Seguimentos PODEM FORMAR um triângulo EQUILÁTERO')
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print('Os Seguimentos PODEM FORMAR Um triângulo ESCALENO')
    else:
        print('Os Seguimentos PODEM FORMAR Um triângulo ISÓSELES')
else:
    print('Os Seguimentos acima não PODEM FORMAR um triângulo')
