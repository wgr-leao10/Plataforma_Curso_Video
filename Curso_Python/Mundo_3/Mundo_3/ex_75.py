print("-=" * 25)
print("Análise de Dados de uma Tupla")
print("-=" * 25)
numero_1 = int(input("Digite Um Número: "))
numero_2 = int(input("Digite Outro Número: "))
numero_3 = int(input("Digite Mais Um Número: "))
numero_4 = int(input("Digite o último Número: "))
tupla_numeros = (numero_1, numero_2, numero_3, numero_4)
print(f'Você Digitou os Valores {tupla_numeros}')
print("O valor 9 apareceu ", tupla_numeros.count(9), "Vezes")
if 3 in tupla_numeros:
    print("O valor 3 Apareceu na Posição", tupla_numeros.index(3)+1)
else:
    print("O valor 3 não foi encontrado em nenhuma Posição")
print('Os Valores pares Digitados foram', end=' ')
for n in tupla_numeros:
    if n % 2 == 0:
        print(n, end=' ')
