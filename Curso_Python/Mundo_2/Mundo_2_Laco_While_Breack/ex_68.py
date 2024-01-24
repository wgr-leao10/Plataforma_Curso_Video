from random import randint
computador = randint(0, 11)
print("=-" * 30)
print("Vamos Jogar Par ou Impar")
print("=-" * 30)
vitorias = 1
while True:
    jogador = int(input("Digite um valor: "))
    palpite = str(input(" Par ou Impar [P/I]: "))
    print("=-" * 30)
    total = jogador + computador
    jogada = total
    if jogada % 2 == 0:
        jogada = 'Par'
    else:
        jogada = 'Impar'
    print(f"Você jogou {jogador} e o computador jogou {computador} Total de {total} e deu {jogada}")
    print("=-" * 30)
    if jogador % computador == 0 and palpite == 'P':
        print("Você venceu!! ")
        print("Vamos Jogar novamente...")
    elif jogador % computador != 0 and palpite == 'I':
        print("Você venceu!!")
        print(" Vamos Jogar novamente...")
        vitorias += 1
    else:
        print(f"Game Over! Você venceu {vitorias} partidas")
        break
