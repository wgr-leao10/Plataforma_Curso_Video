from datetime import date
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = ano_nascimento + 18
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    alistamento_menor = 18 - idade
    print(f'Ainda faltam {alistamento_menor} para o Alistamento')
elif idade > 18:
    alistamento_maior = idade - 18
    print(f'Voce deveria ter se alistado há {alistamento_maior} anos')
    print(f'Seu alistamento foi em {ano_alistamento}')
# aqui colocar verificação de se é masculino ou feminino.
