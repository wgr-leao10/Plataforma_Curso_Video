print('--' * 20)
print('CALCULANDO SEU IMC')
print('--' * 20)
p = float(input('Digite seu Peso (Kg): '))
a = float(input('Digite sua Altura(M): '))
imc = p / (a ** 2)
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do PESO NORMAL')
elif imc > 18.5 and imc < 25:
    print('PARABÉNS, você esta com PESO NORMAL')
elif imc > 25 and imc < 30:
    print('CUIDADO, você esta com SOBREPESO')
elif imc > 30 and imc < 40:
    print('PROCURE AJUDA, você está com OBSIDADE')
else:
    print('CUIDE-SE, você está com OBSIDADE MORBIDA')
