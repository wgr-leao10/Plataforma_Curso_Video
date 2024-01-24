print("-" * 25)
print("GERADOR DE Número")
print("-" * 25)
x = 0
soma = 0
cont = 0
maior = 0
menor = 0
while x != "N":
        n = int(input("Digite um numero: "))
        x = ' '
        while x not in 'SN':
                x = str(input(" Deseja Continuar [S/N] :")).strip().upper()[0]
        soma = soma + n
        cont += 1
        media = soma / cont
        if cont == 1:
                maior = menor = n
        else:
                if n > maior:
                        maior = n
                elif n < menor:
                        menor = n 
print(f"Você digitou {cont}, a médio entre eles é {media:.2f}")
print(f" O maior valor {maior} e o menor valor {menor}")
