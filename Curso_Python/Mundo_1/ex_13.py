print("-=" * 35)
print("Calculadora de Reajuste de Salário")
print("-=" * 35)
salario = float(input("Qual seu salário atual R$: "))
indece_de_reajuste = 0.15
salario_atual = salario + (salario * indece_de_reajuste)
print(f"Um funcionário que ganha R${salario:.2f}, com umm rejuste de 15%, passa a receber R${salario_atual:.2f}")
print("-=" * 35)
