print("-=" * 25)
print("Número por extenso")
print("-=" * 25)

contagem = ("zero", "Um", "Dois", "Três", "Quatro",
            "Cinco", "Seis", "Sete", "Oito", "Nove",
            "Dez", "Onze", "Doze", "Treze", "Catorze",
            "Quinze", "Dezesseis", "Dezessete", "Dezoito",
            "Desenove", "Vinte")
while True:
    num = int(input("Informe um Número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente Novamente.", end=" ")
print(f"Voce Digitou o número {contagem[num]}")
while True:
    resposta = str(input("Voê Deseja Continuar(S/N): ")).strip().upper()[0]
    if resposta == "S":
        print("Continuar")
        break
while True:
    num = int(input("Informe um número de 0 a 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente.")
print(f"Você Digitou o número {contagem[num]}")
#  corrigir este exercicio
