print('=' * 20, 'LOJAS GUANABARA', '=' * 20)
preco = int(input('Preço da Compra R$: '))
print('FORMAS DE PAGAMENTO')
print('[1] á vista Dinheiro/Cheque')
print('[2] á vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é sua opção: '))

if opcao == 1:
    preco_avista = preco * 0.90
    print(f'Sua a compraR${preco} vai custar R${preco_avista:.2f} no final')
elif opcao == 2:
    preco_avista_crto = preco * 0.95
    print(f'Sua compra R$ {preco}vai custar R${preco_avista_crto:.2f}no final')
elif opcao == 3:
    preco_parcelado = preco / 2
    print(f'Sua compraR${preco}vai custar 2X R${preco_parcelado:.2f}SEM JUROS')
elif opcao == 4:
    parcela = int(input('Quantas Parcelas: '))
    preco_parcelado_2 = preco * 1.20
    valor_parcelas = preco_parcelado_2 / parcela
    print(f'Sua compra será parcelada emR${parcela}X deR${valor_parcelas:.2f}')
    print(f'Sua compra de R${preco} vai custar R${preco_parcelado_2} no final')
else:
    print('OPCÇÂO INVÁLIDA!!!')
