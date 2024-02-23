from math import hypot
print("-=" * 15)
print("Cáculo da HIPOTENUSA")
print("-=" * 15)
cateto_x = float(input("Informe o valor do cateto x: "))
cateto_y = float(input("Informe o valor do cateto y: "))
hipotenusa = hypot(cateto_x, cateto_y)
print(f"A hipotenusa é {hipotenusa:.2f}")
print("-=" * 15)
