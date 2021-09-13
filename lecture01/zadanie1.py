import math
b=float( input ("Длина первой стороны b=   "))
C=float( input ("Длина второй стороны c=  "))
d=float( input ("Введите величину угла d= "))
a=(pow(float(C),2))+(pow(float(b),2))-(2*(float(b))*(float(C))*(math.cos(math.radians(d))))
math.cos(float(d))
print("d=", math.cos(float(d)))
print("a=", math.sqrt(a))
