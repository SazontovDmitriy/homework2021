from random import randint
a=input("Введите количество чисел: ")#Вводим количество чисел пользователем
try: #проверка ввода пользователя
    n = int(a)
except ValueError as e:
    print("Error: ", e)
    exit()
numbers = [] #создаем список для вывода чисел

for i in range(int(a)):
    numbers.append(randint(0, int(a))) #Вводим рандомные значения для чисел
    print(numbers)#вывод конечного значения