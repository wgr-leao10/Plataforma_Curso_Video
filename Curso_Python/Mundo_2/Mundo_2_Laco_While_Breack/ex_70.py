print("=-" * 30)
print("LOJA SUPER BARATÃO")
print("=-" * 30)
total_compra = 0
totalmil = 0
cont = 0
menor = 0
barato = ' '
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço do Produto R$: "))
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    total_compra = total_compra + preco
    if preco >= 1000:
        pruduto_mais_1000 = preco
        totalmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if confirmar == 'N':
        break
print(f"Total da compra foi de R$ {total_compra:.2f}")
print(f"Temos {totalmil} pruduto custando mais de R$ 1000.00")
print(f"O pruduto mais barato foi {barato} que custa {menor}")