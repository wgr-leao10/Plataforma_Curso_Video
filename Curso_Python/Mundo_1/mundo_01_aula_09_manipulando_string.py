frase = "Curso em Video Python"

# frase = "curso em video python" # atribuição de uma string para uma variável
print(frase)
print(frase[9])  # Fatiamento
print(frase[9:21])  # Fatiamento em um intervalo
print(frase[9:21:2])  # Fatiamento em um intervalo com pausa
print(frase[15:])  # Fatiamento quando nao sabe o final
print(frase[:5])  # Fatiamento quando nao sabe o inicio
print(frase[9::3])  # Fatiamento quando nao sabe o final com intervalo

# Análise de uma estring
print(len(frase))  # Comprimento da string
print(frase.count("o"))  # conta quantas vezes repetio a letra " o "
print(frase.count("o", 0, 13))  # conta as repeticoes a letra "o",no intervalo
print(frase.find("deo"))  # aqui indcia onde inicia a string
print(frase.find("Androide"))  # quando não encontra ele devolve -1.
print("curso" in frase)

# Transformação
print(frase.replace("Python", "Android"))
print(frase.upper())  # Todas Maiúculas
print(frase.lower())  # Todas Minusculas
print(frase.capitalize())  # Só as primneras letras maisculas
print(frase.title())  # Analiosa os blocos e coloca as primeras maiúsculas
print(frase.strip())  # Elimina os espaços do inicio e do final
print(frase.rstrip)  # Elimina os espaços do do lado direito
print(frase.rstrip())  # Elimina os espaços do do lado direito
print(frase.lstrip())  # Elimina os espaços do do lado esquerdo

# Divisão
print(frase.split())  # Aqui divede a string
print("-".join(frase))  # Aqui junta os caracteres
