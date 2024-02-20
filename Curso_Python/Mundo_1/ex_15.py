print("-=" * 35)
print("Cáculo do Aluguel")
print("-=" * 35)
km = float(input("Quantos Km Rodados: "))
dias_usado = int(input("Quantos dias Alugados: "))
valor_diario = 60
valor_km = 0.15
caculo_aluguel = (km * valor_km) + (dias_usado * valor_diario)
print(f"O valor total do Aluguel é R$: {caculo_aluguel:.2f}")
