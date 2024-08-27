def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Função Votar Ex_101":^40}'))


def votar(ano_nacimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual- ano_nacimento


idade = votar(ano_nacimento = int(input("Qual o ano do seu nascimento?:")))
if idade < 16:
    print(f'Com{idade} anos:NEGATO')
elif 16 <= idade < 18 or idade >= 65:
    print(f'Com {idade} anos: OPCIONAL')
else:
    print(f'Com {idade} anos: OBRIGATóRIO')
