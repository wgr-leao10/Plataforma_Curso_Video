from datetime import date
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'O Atleta tem {idade} Anos')
if idade <= 9:
    print('Classificação: Mirim')
elif idade > 9 and idade <= 14:
    print('Classificação: Infantil')
elif idade > 14 and idade <= 19:
    print('Classificação: Junior')
elif idade > 19 and idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')
