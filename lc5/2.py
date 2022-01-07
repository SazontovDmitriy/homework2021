class d_exception(Exception):
    def __init__(self, text):
        self.txt = text


while True:
    try:
        key = input("Введите строку формата NdM, где N - количество кубиков, а M - количество сторон каждого из них: ")
        if 'd' not in key:
            raise d_exception("char 'd' is not in keyword")
        N = int(key[0])
        M = int(key[2:])
        cubes = [[x + 1 for x in range(M)] for _ in range(N)]
        break
    except Exception as e:
        print("Неправильный ввод, введите строку снова. Ошибка:", e)


s = [0]
for i in range(len(cubes)):
    cmb = [a + b for a in s for b in cubes[i]]
    s = [x for x in cmb]


for x in sorted((set(s))):
    print(x, '=', round(s.count(x)/len(s) * 100, 2), "%")
    # print(x, '=', s.count(x) / len(s) * 100, "%")
