def fat(x):
    if x == 1:  # caso base
        return 1
    else:
        return x * fat(x - 1)  # caso recursivo
