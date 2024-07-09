print("-" * 40)
print(f'{"Cadastro de Trabalho EX_92":^40}')
print("-" * 40)
trabalhadores = dict()

from datetime import datetime
trabalhadores['Nome'] = str(input("Nome: "))
trabalhadores['Nascimento'] = int(input("Ano de Nascimento: "))

trabalhadores['CTS'] = int(input("Carteira de Trabalho: "))
trabalhadores["contratação"] = int(input("Ano de contratação: "))
trabalhadores['Salário'] = float(input("Salário: "))

trabalhadores['Idade'] = datetime.now().year - trabalhadores["Nascimento"]
trabalhadores['CTPS'] = int(input("Carteira de Trabalho (0 Não Tem): "))
if trabalhadores["CTPS"] == 0:
    print(f'Nome Tem Valor {trabalhadores["Nome"]}')
    print(f'Idade Tem Valor {trabalhadores["Idade"]} Anos')
    print(f'CTPS Tem Valor {trabalhadores["CTPS"]}')
else:
    trabalhadores["contratação"] = int(input("Ano de contratação: "))
    trabalhadores['Salário'] = float(input("Salário R$: "))
    trabalhadores['Aposentadoria'] = trabalhadores["Idade"] + (35 + trabalhadores['contratação']) - datetime.now().year
    print(f'Nome Tem Valor {trabalhadores["Nome"]}')
    print(f'Idade Tem Valor {trabalhadores["Idade"]} Anos')
    print(f'CTPS Tem Valor {trabalhadores["CTPS"]}')
    print(f'Contratação Tem Valor {trabalhadores["contratação"]}')
    print(f'Salário Tem Valor R${trabalhadores["Salário"]:.2f}')
    print(f'Aposentadoria Tem valor {trabalhadores["Aposentadoria"]}')
print("-" * 40)
