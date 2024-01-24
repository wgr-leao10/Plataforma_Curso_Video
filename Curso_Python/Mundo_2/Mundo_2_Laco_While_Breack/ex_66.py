n = s = cont = 0
while True:
    n = int(input("Digite ume número: "))
    if n == 999:
        break
    cont += 1
    s += n
print(f"A quantidade de números são {cont}, e a soma entre eles {s}")
