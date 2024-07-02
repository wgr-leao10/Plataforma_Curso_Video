print("-" * 40)
print(f'{"Situação do aluno EX_90_Refatorado":^40}')
print("-" * 40)
alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f"Média: de {alunos['Nome']}: "))
if alunos['Média'] >= 7:
    alunos["Situação"] = "Aprovado"
elif 5 < alunos["Média"] < 7:
    alunos["Situação"] = "Recuperação"
else:
    alunos["Situação"] = "Reprovado"
for i, j in alunos.items():
    print(f"{i} é igual a {j}")
print("-" * 40)
