print("-" * 30)
print("Contador de Número")
print("-" * 30)
n = 0
soma = 0
cont = 0
while True:
    n = int(input("Dgite um numero [999 para parar]: "))
    soma = soma + n
    cont += 1
    if n == 999:
        break
print(f"Você digitou {cont} e a soma entre eles foi {soma}")
