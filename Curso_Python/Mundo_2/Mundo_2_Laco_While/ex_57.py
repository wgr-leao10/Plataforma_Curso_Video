x = str(input("Infome seu sexo [M/F]:")).strip().upper()[0]
while x not in 'MnFf':
    x = str(input("Dados inválidos. Por Favor, informe seu sexo correto: ")).strip().upper()[0]
print(f"Sexo {x} registrado com sucesso")
