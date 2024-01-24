from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for i in range(1, 8):
    nascimento = int(input("Em que ano {}° a pessoa nasceu?: ".format(i)))
    idade = ano_atual - nascimento
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print(f"A o todo tivemos {cont_maior} pessoas maiores de idade")
print(f"E também tivemos {cont_menor} pessoas menor de idade")
