# 5 Задание
print("")
print("Обработка исключения KeyError")
dictionary = {
    1: "Hello",
    2: "World",
}
try:
    print(dictionary[3])
except KeyError as e:
    print("Такого Элемента нет в словаре")