def titulo(txt):
    print("-" * 40)
    print(txt)
    print("-" * 40)


titulo((f'{"Função Votar Ex_101":^40}'))


def votar(ano_nacimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nacimento
    if idade < 16:
        return f'Com {idade} anos:NEGATO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATóRIO'


nasc = int(input("Qual o ano do seu nascimento?:"))
print(votar(nasc))
