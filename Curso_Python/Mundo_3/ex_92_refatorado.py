print("-" * 40)
print(f'{"Cadastro de Trabalho EX_92_Refatorado":^40}')
print("-" * 40)
trabalhadores = dict()
from datetime import datetime
trabalhadores['Nome'] = str(input("Nome: "))
trabalhadores['Nascimento'] = int(input("Ano de Nascimento: "))
trabalhadores['Idade'] = datetime.now().year - trabalhadores["Nascimento"]
trabalhadores['CTPS'] = int(input("Carteira de Trabalho (0 Não Tem): "))
if trabalhadores["CTPS"] != 0:
    trabalhadores["contratação"] = int(input("Ano de contratação: "))
    trabalhadores['Salário'] = float(input("Salário R$: "))
    trabalhadores['Aposentadoria'] = trabalhadores["Idade"] + (35 + trabalhadores['contratação']) - datetime.now().year
print("-" * 40)
for i, j in trabalhadores.items():
    print(f' {i} Tem Valor {j}')
