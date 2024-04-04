print("-=" * 25)
print("Qual o Maior Número?")
print("-=" * 25)
num_1 = int(input("Primeiro Valor: "))
num_2 = int(input("Segundo Valor: "))
num_3 = int(input("Terceiro Valor: "))
if num_1 > num_2 and num_1 > num_3:
    print(f"O Maior Valor Digititado {num_1}")
if num_2 > num_1 and num_2 > num_3:
    print(f"O Maior Valor Digititado {num_2}")
if num_3 > num_1 and num_3 > num_2:
    print(f"O Maior Valor Digitado {num_3}")
if num_1 < num_2 and num_1 < num_3:
    print(f"O Menor Valor Digititado {num_1}")
if num_2 < num_1 and num_2 < num_3:
    print(f"O Menor Valor Digititado {num_2}")
if num_3 < num_1 and num_3 < num_2:
    print(f"O Menor Valor Digitado {num_3}")
print("Bom Dia")
