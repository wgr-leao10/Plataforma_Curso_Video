galera = list()  # Lista principal
dado = list()  # lista para guarda os dados temporárimente
totalmaior = totalmenor = 0  # só pode ser com variável simples
for c in range(0, 3):  # aqui seria a estrutura para lê gravar dados na lista
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:  # Aqui seria a verificação da idade
    if p[1] >= 21:
        print(f"{p[0]}é maior de idade ")
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')
