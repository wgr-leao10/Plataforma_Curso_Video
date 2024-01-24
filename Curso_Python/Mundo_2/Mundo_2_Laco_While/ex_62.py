print("=" * 20)
print("Gerador de PA")
print("=" * 20)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro_termo
cont = 1
mais_termo = 10
total = 0
while mais_termo != 0:
    total = total + mais_termo
    while cont <= total:
        termo = termo + razao
        print(f"{termo}", end=" = ")
        cont += 1
    print("PAUSA...")
    mais_termo = int(input("Quantos termos você quer mostrar: "))
print(f"Progreção finalizada com {total} termos")
