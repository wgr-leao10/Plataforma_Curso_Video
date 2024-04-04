print("-=" * 25)
print("Cáculo de Salário?")
print("-=" * 25)
salario_funcionario = float(input("Qual o Salário Do Funcionário R$ "))
if salario_funcionario <= 1250:
    salario_novo = salario_funcionario * 1.15
if salario_funcionario > 1250:
    salario_novo = salario_funcionario * 1.10
print(f"Quem Ganhava R${salario_funcionario:.2f} passa a ganhar R${salario_novo:.2f}")
