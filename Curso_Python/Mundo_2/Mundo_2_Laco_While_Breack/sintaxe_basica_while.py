# cont = 1
# while cont < 11:
#    print(cont)
#    cont += 1
# print("Acabou")
# Execução básica do código

# Codigo usando o comando breack
n = s = 0
while True:
    n = int(input("Digite um númerro: "))
    if n == 999:
        break
    s += n
print(f"Acabou, a soma dos números {s}")

# A diferente entere o código anterior e este 
# seria uma execução a mais 
# pois com a atribuição do s-= 999 vai fazer mais um operação
n = s = 0
while n != 999:
    n = int(input("Digite um númerro: "))
    s += n
s -= 999
print(f"Acabou, a soma dos números {s}")
