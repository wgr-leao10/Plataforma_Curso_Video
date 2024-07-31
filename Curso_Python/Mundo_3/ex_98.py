from time import sleep


def titulo(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


titulo((f'{'Função de Contador Ex_98':^40}'))


def contador(inicio, fim, passo):
    sleep(1.5)

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio

        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            cont += passo
        print(" Fim! ")
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            cont -= passo
        print('Fim!')


#  programa principal
titulo((f'{"Contagem de 1 até 10 de 1 em 1"}'))
contador(0, 11, 1)
sleep(0.5)
print()

titulo((f"{'Contagem de 10 até 0 de 2 em 2'}"))
contador(10, 0, 2)
sleep(0.5)
print()

titulo((f'{'Agora é sua vez de Personalizar a Contagem!'}'))
inicio = int(input("Ìnicio: "))
fim = int(input('FIM: '))
passo = int(input("Passo: "))
print()
titulo((f'{f"Contagem de {inicio} até {fim} de {passo} em {passo}"}'))
contador(inicio, fim, passo)

print()
