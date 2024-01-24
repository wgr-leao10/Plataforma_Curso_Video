print("=" * 20)
print("10 PRIMEIROS TERMOS DE UMA PA")
print("=" * 20)
primero_termo = int(input("Primeiro Termo: "))
razao = int(input("Razâo: "))
termo = primero_termo
cont = 1
while cont < 11:
        termo = termo + razao
        cont += 1
        print(f"{termo}", end=' = ')
print("Acabou...")
