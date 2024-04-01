from datetime import date
print("-=" * 25)
print("O Ano é Bissexto?")
print("-=" * 25)
ano = int(input("Que Ano quer Analisar? Se for 0 analisa ano Atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto")
else:
    print(f"O ano {ano} não é Bissexto")
