print("=" * 20)
print("Gerador de PA")
print("=" * 20)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo = termo + razao
        print(f"{termo}", end=" = ")
        cont += 1
    print("PAUSA...")
    mais = int(input("Quantos termos você quer mostrar: "))
print(f"Progreção finalizada com {total} termos")
