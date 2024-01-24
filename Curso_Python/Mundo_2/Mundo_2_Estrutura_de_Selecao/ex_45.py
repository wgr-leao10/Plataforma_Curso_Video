from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas Opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-=' * 20)
print(f'O Computador escolheu {(itens[computador])}')
print(f'Jogador escolheu {(itens[jogador])}')
print('=-=' * 20)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Computador Vence')
elif computador == 1:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
elif computador == 2:
    if jogador == 0:
        print('jogador Vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
if jogador < 0 or jogador > 2:
    print('Joagada inválida')
