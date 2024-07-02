print("-" * 40)
print(f'{"Situação do aluno EX_90":^40}')
print("-" * 40)
alunos = dict()

alunos['Nome'] = str(input("Nome: "))
alunos['Media'] = float(input("Média: "))

if alunos["Media"] >= 7:
    alunos["Situação"] = "Aprovado"
    print(f"O nome é igual a {alunos['Nome']}")
    print(f"Média é igual a {alunos['Media']}")
    print(f'Situação é igual a {alunos["Situação"]}')
elif 5 < alunos["Media"] < 7:
    alunos["Situação"] = "Recuperação"
    print(f"O nome é igual a {alunos['Nome']}")
    print(f"Média é igual a {alunos['Media']}")
    print(f'Situação é igual a {alunos['Situação']}')
else:
    alunos["Situação"] = "Reprovado"
    print(f"O nome é igual a {alunos['Nome']}")
    print(f"Média é igual a {alunos['Media']}")
    print(f"Situação é igual a {alunos['Situação']}")
print("-" * 40)
