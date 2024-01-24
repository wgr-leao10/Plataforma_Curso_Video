print("-" * 25)
print("Sequência de Fibonacci")
print('-' * 25)
n = int(input("Quantos termos você quer mostrar: "))
t1 = 0
t2 = 1
print("-" * 25)
print(f"{t1}", end=" - ")
print(f"{t2}", end=" - ")
cont = 3
while cont <= n:
    resultado = t1 + t2
    cont += 1
    print(f"{resultado}", end=" - ")
    t1 = t2
    t2 = resultado
print("Fim")
print("-" * 25)
