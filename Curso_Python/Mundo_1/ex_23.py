print("-=" * 15)
print("Analisando Numero")
print("-=" * 15)
num = int(input("Informe seu Número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o Número {num}")
print(f"Unidade: {u} ")
print(f"Dezena: {d}")
print(f"Centena:{c}")
print(f"Milhar: {m}")
