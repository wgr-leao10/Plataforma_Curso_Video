from random import randint
computador = randint(0, 10)
print("Sou seu computador ...Acabei de pensar em um numero de 0 a 10")
print("Será que oê consegue adivinhar, qual foi ?")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?: "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos..")
print("Acertou!!, com {palpite} palpites")
