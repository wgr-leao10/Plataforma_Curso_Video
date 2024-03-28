print("-=" * 15)
print("Analisando Nome")
print("-=" * 15)
nome = str(input("Digite seu Nome:")).strip()
partes_do_nome = nome.split()
primerio_nome = partes_do_nome[0]
print("Seu Nome em Maiúculo é", nome.upper())
print("Seu Nome em Minisculo é", nome.lower())
print("Seu nome tem ao todo ", len(nome) - nome.count(' '))
print(f"Seu primeiro nome é {primerio_nome}", "e o tem ", len(primerio_nome), "Letras")
#  Forma alternativa
#  print("Seu primeiro nome é", nome.split()[0], "e o tem ", nome.find(' '), "Letras") 
