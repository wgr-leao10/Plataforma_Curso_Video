print("**" * 35)
print("Calculadora de Tinta")
print("**" * 35)
largura = float(input("Largura da Parede em Metros: "))
altura = float(input("Altura da Parede em metros: "))
area = largura * altura
indece_de_pintura = 2
quantidade_de_tinta = area / indece_de_pintura
print(f"Sua Parede tem dimensãoes de {largura}x{altura}M e a área é {area:.3f}M")
print(f"Para pintar essa parede, vc precisará de {quantidade_de_tinta:.3f}L de tinta")
print("**" * 35)
