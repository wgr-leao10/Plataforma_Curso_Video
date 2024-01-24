valor_casa = float(input('Valor Da Casa R$  '))
salario = float(input('Salário Do Comprador R$  '))
tempo = int(input('Tempo De Finaciamento ?  '))
prestação = (valor_casa / tempo) / 12
condicao_aprovacao = (prestação / salario) * 100
if condicao_aprovacao > 30:
    print(f'Para Pagar Uma Casa de {valor_casa} Em {tempo}')
    print(f'A Prestação Será De{prestação:.2f}')
    print('Empréstimo NEGADO!!!')
else:
    print(f'Para Pagar um casa de {valor_casa} Em {tempo}')
    print(f'A Prestação Será De: {prestação:.2f}')
    print('Empréstimo APROVADO!!')
print('Volte Sempre!!!')
