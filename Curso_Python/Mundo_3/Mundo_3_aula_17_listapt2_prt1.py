galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])  # localização com o índice
print(galera[1][0])
print(galera[2][1])
print(galera[2][0])
print(galera[3][0])
for p in galera:
    print(f"{p[0]}tem {p[1]} anos de idade")  # Aqui so print do indice 0
    print(p[1])  # Aqui so print do indice 1, e formatado
