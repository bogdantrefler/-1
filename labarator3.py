a = True
spisok = []
spisok2 = []
slovnik = {
    "rating":None,
    "name":None
}
good = []
norm = []
bad = []
print("це список студентів та їх оцінок,\n для зупинки введіть stop у розділі введіть ім'я студента\n максимальна оцінка 12 мінімальна оцінка 0")
while a:
    it=input("Ввдіть ім'я студента ")
    it1 = int(input("Введіть оцінку студента"))
    yoour = slovnik["rating"] = it,it1
    spisok.append(yoour)
    spisok2.append(it1)
    if it1 <=6:
        bad.append(it)
        bad.append(it1)
        if it == "stop":
            bad.pop()
            bad.pop()
    elif it1 <= 9 :
        norm.append(it)
        norm.append(it1)
        if it == "stop":
            norm.pop()
            norm.pop()
    else :
        good.append(it)
        good.append(it1)
        if it == "stop":
            good.pop()
            good.pop()
    if it1 > 12 or it1 < 0:
        print("Оцінку було введено не правильно")
    if it == ("stop" or it1 == "stop"):
        spisok.pop()
        a = False
result = sum(spisok2) / len(spisok2)
print(spisok , "\n\n середнє значення ", result , "\n\n погана статистика ", bad , "\n нормальний результат", norm ,"\n чудовий результат",good)


