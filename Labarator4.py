goods = {
    "хліб": True,
    "Молоко": True,
    "яйця": False,
    "сир": True,
    "яблука": True,
    "банани": False,
    "виноград": True,
    "апельсини": True,
    "огірки": False,
    "помідори": True,
    "картопля": True,
    "морква": True,
    "цибуля": True,
}
price = {
    "хліб": 25.5,
    "Молоко": 32.0,
    "яйця": 45.0,
    "сир": 80.0,
    "яблука": 15.75,
    "банани": 20.0,
    "виноград": 50.0,
    "апельсини": 30.0,
    "огірки": 18.0,
    "помідори": 22.0,
    "картопля": 12.0,
    "морква": 14.0,
    "цибуля": 10.0,
}
price_get = []


def purchase_goods():
    print("якщо ви закінчили покупку просто введіть 'stop'")
    a = True
    while a:
        item = input("введіть товар який хочете купити:")
        price_get.append(item)
        ter = price.get(item)
        if item == "stop":
            a = False
            price_get.pop()
            print(ter)

            print("ваш список товарів ", price_get)


def tovar(*items):
    result = {}
    for item in items:
        if item in goods:
            result[item] = goods[item]
        else:
            result[item] = False
    return result


purchase_goods()
ava = tovar(*price_get)
total = 0
for item, is_ava in ava.items():
    if is_ava:
        total += price[item]


def kroch(money):
    return f"ціна: {money:.2f}грн"


print("Перевірка наявності вашого товару з списку ", ava)
print(f"ціна доступних товарів:", kroch(total))

