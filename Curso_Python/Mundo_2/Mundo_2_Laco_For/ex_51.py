print("=" * 20)
print("10 TERMOS DE UMA PA")
print("="*20)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
for i in range(1, 11):
    primeiro_termo += razao
    print(f"{primeiro_termo}", end=' = ')
print("Acabou")
