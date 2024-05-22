print("-" * 40)
print(f'{"Lista Composto e Análise de Dados EX_83":^40}')
print("-" * 40)
cadastro = list()
dados = list()
i = totalcadastro = maiorpeso = menorpeso = 0
while i != 'N':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        maiorpeso = menorpeso = cadastro[1]
    else:
        if cadastro[1] > maiorpeso:
            maiorpeso = cadastro[1]
        if cadastro[1] < menorpeso:
            menorpeso = cadastro[1]
    cadastro.append(dados[:])
    dados.clear()
    i = ' '
    while i not in 'SN':
        i = str(input('Deseja Continuar [S/N]')).strip().upper()[0]
    totalcadastro += 1
print(f'Ao todo as pessoas cadastrados{cadastro}')
print(f'A todo, você cadastrou {totalcadastro} pessoas')
print(f'O maior peso foi {maiorpeso}')
print(f'O menor peso foi {menorpeso}')
print("-" * 40)
# falta corrigir esta parte 