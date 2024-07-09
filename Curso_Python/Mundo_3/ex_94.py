print("-" * 40)
print(f'{"Unindo Os Dicionários EX_94":^40}')
print("-" * 40)
pessoas = list()
cadastro_pessoas = dict()
cont_pessoas = soma_idade = 0
while True:
    cadastro_pessoas["nome"] = str(input('Nome: ')).strip()
    cont_pessoas += 1

    while True:
        cadastro_pessoas["sexo"] = str(input("Sexo[M/F]: ")).strip().upper()[0]
        if cadastro_pessoas["sexo"] in ('M', 'F'):
            break
        print('Digite Apenas M ou F')

    cadastro_pessoas['idade'] = int(input("Idade: "))
    soma_idade += cadastro_pessoas["idade"]
    media_idade = soma_idade / cont_pessoas

    while True:
        cadastro_pessoas['resposta'] = input("Deseja continuar [S/N]: ").strip().upper()
        if cadastro_pessoas["resposta"] in ('S', 'N'):
            break
        print('Digite apenas S ou N')

    pessoas.append(cadastro_pessoas.copy())

    if cadastro_pessoas["resposta"] == 'N':
        break
print(f'A) Ao todo temos {cont_pessoas} pessoas Cadastradas')
print(f'b) A Média de Idade é {media_idade:.2f}')
print(' c) As mulheres Cadastradas foram', end=" ")
for p in pessoas:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print("D) Lista de Pessoas que estão acima da media:")
for i in pessoas:
    if p['idade'] >= media_idade:
        print(f'nome = {p["nome"]}; sexo = {p['sexo']}; idade = {p['idade']}', end=' ')
        print()
print('ENCERRADO...')
print("-=" * 40)
