print("-=" * 30)
print("CADASTRE UMA PESSOA")
print("-=" * 30)
maiores_de_18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if idade > 18:
        maiores_de_18 += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    if confirmar == 'N':
        break
print("=-" * 30)
print(f"Tota de pessoas com mais de 18 anos: {maiores_de_18}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres} mulheres com menos de 20 anos")
