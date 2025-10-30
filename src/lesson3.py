from itertools import accumulate

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))


d = b**2 - 4*a*c

if a == 0:
    raise ZeroDivisionError ("На ноль делить нельзя")
if d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / (2*a)
    print(x)
else:
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)
    print(x1, x2)