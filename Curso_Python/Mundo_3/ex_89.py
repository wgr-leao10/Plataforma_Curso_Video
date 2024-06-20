print("-" * 40)
print(f'{"Boletim com Listas Compostas EX_89":^40}')
print("-" * 40)
dados = list()
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1:')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja Continuar[S/N]'))
    if resp in "Nn":
        break
print(f"{"N°":<4}{"Nome":<10}{"Média":>8}")
print(('-' * 26))
for i, j in enumerate(dados):
    print(f"{i:<4}{j[0]:<10}{j[2]:>8.1f}")
    while True:
        opc = str(input("Mostrar nota de qual aluno(999 interompe): "))
        if opc == 999:
            print("FINALIZADO")
            break
        if opc <= len(dados) - 1:  # Ver o errro 
            print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
while True:
    opc = int(input("Mostrar nota de qual aluno(999 interompe): "))
    if opc == 999:
        print("FINALIZADO")
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
    else:
        print('Indice Iválido')
print("**** Volte Sempre****")
print("-" * 50)
