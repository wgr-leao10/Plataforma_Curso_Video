#  exemplo de condição ssimples

#  nome = str(input("Digite seu nome: "))
#  if nome == "Gustavo:"
#     print("Que nome lindo voç~e tem!!")
#  print ("Bom dia ")

#  exemplo de condição Composta

print("-=" * 25)
print("Cáculo da Média e Avaliação Final")
print("-=" * 25)
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))
media = (nota1 + nota2) / 2
if media >= 6.5:
    print(f"Sua nota foi {media}, está APROVADO")
else:
    print(f"Sua nota foi {media}, está REPROVADO")
print("BOM DIA")
