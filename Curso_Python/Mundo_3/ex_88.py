from random import randint
from time import sleep
print("-" * 40)
print(f'{"Palpites Para Mega Sena EX_88":^40}')
print("-" * 40)
lista = []
jogo = []
tot = 1
quant = int(input("Quantos Jogos você quer que eu sorteie: "))
print(f'=-= Sorteando os {quant} Jogos =-=')
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1  # controla qt° de sujestoes
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1  # quat° jogos
for i, j in enumerate(jogo):
    print(f"Jogo: {i+1} : {j}")
    sleep(1)
print('*' * 10, "Boa Sorte", "*" * 10)
print("-" * 40)
