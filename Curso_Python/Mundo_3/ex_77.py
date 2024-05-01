print("-" * 40)
print(f'{"ENCONTRAR VOGAIS EX_77":^40}')
print("-" * 40)
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR'
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\n Na Palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end='',)
print('\n', "-" * 40)
