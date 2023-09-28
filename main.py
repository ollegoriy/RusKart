spisok = [3, 7, 8, 4, 1, 7, 6]
spisok1 = ["Mon", "Fri", "Sat"]
print("Сумма элементов списка:", sum(spisok))
print("Наибольший элемент:", max(spisok))
print("Список без дубликатов:", set(spisok))
spisok2 = spisok + spisok1
print("Объединенный список:", spisok2)
def search(a, b):
    if b in a:
        return a.index(b)
    else:
        return "Элемент не найден"
def fusion(a, b):
    x = list(a)
    y = list(b)
    xy = x + y
    xy = tuple(xy)
    return xy
def removing(a, b):
    x = list(a)
    if b in a:
        x.remove(b)
        y = tuple(x)
        return y
    else:
        return "Элемент не найден"
def quantity(a, b):
    if b in a:
        x = 0
        for i in a:
            if i == b:
                x += 1
            else:
                continue
        return x
    else:
        return "Элемент не найден"
kortezh = (5, 8, 7, 3, 9, 6, 7)
kortezh1 = ("Aventador", "Revuelto", "Urus")
print("Поиск элемента:", search(kortezh, 3))
kortezh2 = fusion(kortezh, kortezh1)
print("Слияние кортежей:", kortezh2)
print("Удаление элемента:", removing(kortezh1, "Urus"))
print("Подсчет элементов:", quantity(kortezh, 7))

