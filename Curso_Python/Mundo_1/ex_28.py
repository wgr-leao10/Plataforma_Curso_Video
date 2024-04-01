from random import randint
print("-=" * 25)
print("VOU PENSAR EM UM NÚMERO DE 0 A 5. TENTE ADIVINHAR....")
print("-=" * 25)
jogador = int(input("Em que numero eu pensei?: "))
computador = randint(0, 5)
if jogador == computador:
    print(f"PARABENS! Você consegiu venceu!, eu pensei {computador}")
else:
    print(f"TENTE NOVAMENTE, pois eu pensei {computador}")
