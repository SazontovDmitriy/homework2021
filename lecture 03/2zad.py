d: str=(input("Введите число а="))
f=input ('Введите число b= ')
try:
    a = int(d)
    b= int(f)
except ValueError as e:
    print("Error: ", e)
    exit()
while int(d) != 0 and int(f) != 0:
    if int(d) > int(f):
        d = int(d) % int(f)
    else:
        f = int(f) % int(d)
print(int(f) + int(d))