from random import randint
print("-=" * 25)
print("Sorteio de Números")
print("-=" * 25)
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(f'Os Numeros sorteados são:{sorteio}')
print(f'O maior valor Sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
