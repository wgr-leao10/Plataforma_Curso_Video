primeiro_numero = int(input("Digite o Primeiro Valor: "))
segundo_numero = int(input("Digite o Segundo Valor: "))
while True:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Números")
    print("[5] Sair do Programa")
    print(">" * 5, "Qual Sua opção")

    opcao = int(input("Digite sua Opção: "))

    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print(f"O resultado de {primeiro_numero} + {segundo_numero} é igual {soma}")
        print("=-" * 10)
    elif opcao == 2:
        mutiplicar = primeiro_numero * segundo_numero
        print(f"O resultado de {primeiro_numero} x {segundo_numero} é igual {mutiplicar}")
        print("=-" * 10)
    elif opcao == 3:
        if primeiro_numero > segundo_numero:
            print(f"O resultado de {primeiro_numero} maior que {segundo_numero}")
        else:
            print(f"O resultado de {primeiro_numero} é menor que {segundo_numero}")
        print("=-" * 10)
    elif opcao == 4:
        primeiro_numero = int(input("Digite o Primeiro Valor: "))
        segundo_numero = int(input("Digite o Segundo Valor: "))
    elif opcao == 5:
        print("--Sair do programa--")
        break
    else:
        print("Opção incorreta, digite novemente")
