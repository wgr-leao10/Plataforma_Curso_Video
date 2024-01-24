frase = str(input("Digite uma Frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
print(f"Você Digitou a Frase {junto}")
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("temos um Palíndromo")
else:
    print("A frase não é um Palímdromo")
