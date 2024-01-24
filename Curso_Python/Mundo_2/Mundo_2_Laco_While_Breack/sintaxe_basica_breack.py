# Aqui com o flag de parada deve ser usado o while True
# ele abre um loop infinito onde o breack e determinado pelo  flag
while True:
    x = int(input("Quer ver tabuada de qual Valor: "))
    if x < 0:
        break
    y = 1
    while y < 10:
        tabuada = x * y
        print(f" {x} x {y} = {tabuada}")
        y += 1
print("Programa de tabuada encerrado")
