
print("=" * 20)
print(" --- Cáculo do Fatorial --")
n = int(input("Digite um neumero para calcular o fatorial: "))
j = 1
for i in range(n, 0, -1):
    j *= i
print(f"O fatorial de {n}! é {j}")
