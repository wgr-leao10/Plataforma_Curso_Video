print("**" * 35)
print("Calcularora de Desconto")
print("**" * 35)
preco_produto = float(input("Qual o preço do Produto R$: "))
desconto = 0.05
preco_atual = preco_produto - (preco_produto * desconto)
print(f"O produto que custava R$ {preco_produto:.2f}, na promoção com desconto de 5% vai custar R${preco_atual:.2f}")
print("**" * 35)
