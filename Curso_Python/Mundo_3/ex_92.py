print("-" * 40)
print(f'{"Cadastro de Trabalho EX_92":^40}')
print("-" * 40)
trabalhadores = dict()

trabalhadores['Nome'] = str(input("Nome: "))
trabalhadores['Nascimento'] = int(input("Ano de Nascimento: "))

trabalhadores['CTS'] = int(input("Carteira de Trabalho: "))
trabalhadores["contratação"] = int(input("Ano de contratação: "))
trabalhadores['Salário'] = float(input("Salário: "))

print("-" * 40)
