print("-=" * 25)
print("Cálculo de Passagem")
print("-=" * 25)
distancia_da_viagem = float(input("Qual a Distância da Sua Viagem: "))
print(f"Você está Prestes a Começar Uma Viagem de {distancia_da_viagem}KM")
if distancia_da_viagem == 200:
    valor_passagem = distancia_da_viagem * 0.50
else:
    valor_passagem = distancia_da_viagem * 0.45
print(f" O Preço da Sua Viagem é de R${valor_passagem:.2f}")
