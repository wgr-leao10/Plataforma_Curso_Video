num = int(input("Digite um Número: "))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
        print(f"{i}", end=" ")
print(f"\033[O número {num} foi divisivel {tot}")
if tot == 2:
    print("è por isso que É PRIMO")
else:
    print("è por isso que NâO è PRIMO")    
