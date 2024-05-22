print("-" * 40)
print(f'{"Validando expressões Matemáticas EX_83":^40}')
print("-" * 40)
n = str(input("Digite a Expressão: "))
expressoes = list()
for simb in expressoes:
    if simb == '(':
        expressoes.append('(')
    elif simb == ')':
        if len(expressoes) > 0:
            expressoes.pop()
        else:
            expressoes.append(')')
            break
if len(expressoes) == 0:
    print("Sua expressão é válida")
else:
    print("Sua expressão não é Válida")
print("-" * 40)
