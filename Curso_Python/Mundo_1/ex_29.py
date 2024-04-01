print("-=" * 25)
print("Radar de Velocidade")
print("-=" * 25)
velocidade_atual = int(input("Qual é sua Velocidade Atual do Carro: "))
velocidade_maxima = 80
valo_multa_por_km_excedido = 7
multa = (velocidade_atual - velocidade_maxima) * valo_multa_por_km_excedido
if velocidade_atual > velocidade_maxima:
    print(f"MULTADO! Você excedeu o limite permitido de {velocidade_maxima}KM")
    print(f"Você deve pagar uma multa de R${multa},00")
else:
    print(f"Velocidade de {velocidade_atual}KM Permitida")
print("Tenha um bom dia Dirija com segurança!")
