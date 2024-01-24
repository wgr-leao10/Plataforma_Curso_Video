n = int(input('Digite Um Número Interio: '))
print('Escolha Uma Das Bases Para Conversão: ')
print('[1] Converter Para BINÁRIO')
print('[2] Converter para Octanal')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua Opção é: '))

if opcao == 1:
    print(f'{n} Convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} Convertido para OCTANAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} Convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida Tente Novamente')
