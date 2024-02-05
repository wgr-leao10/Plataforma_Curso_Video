# Aqui estamos estudando os operadores Aritiméticos.
# Mais detalhes no relatória da aula.
# Abaixo um exemplos
print("=-" * 25)
print("Exemplo de Utilização de operadores Numérico")
print("=-" * 25)
n1 = int(input("Digite um Valor: "))
n2 = int(input("Digite um valor: "))
soma = n1 + n2
subtração = n1 - n2
divisão_simples = n1 / n2
divisão_sobra = n1 // n2
divisão_resto = n1 % n2
potencia = n1 ** n2
ordem_de_precedencia = n1 + (n2 * n1) ** n1 - n2 * (n2)
print(f"A soma é: {soma}\n À subtração é: {subtração}")
print(f"A divisão simples:{divisão_simples} \n A Sobras da divisão é:{divisão_sobra}\n O resto da divisão é:{divisão_resto}")
print(f"A ordem de procedencia: {ordem_de_precedencia:.3f}")
print("=-" * 25)
