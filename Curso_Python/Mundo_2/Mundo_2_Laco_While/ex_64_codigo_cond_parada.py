print("-" * 30)
print("Contador de Número")
print("-" * 30)
n = 0
soma = 0
cont = 0
n = int(input("Dgite um numero [999 para parar]: "))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input("Dgite um numero [999 para parar]: "))
print(f"Você digitou {cont} e a soma entre eles foi {soma}")
