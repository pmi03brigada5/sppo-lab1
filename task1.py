
# 1 задание
ints = [1, 2, 3, 4, 5]
strings = ["Hello", "World"]
print("Начальный список с числами", ints)
print("Начальный список со строками", strings)

print("")
print("Срезы:", strings[:2], strings[1:], ints[3:], ints[:4])
print("Реверс:", strings[::-1])

print("")
print("Элементы списка через \":\"", ":".join(strings))

print("")
print("zip:", list(zip(ints, strings)))

print("")
print("Генераторы:\n\tЧисла от 0 до 9:",
    [x for x in range(10)])
print("\tКвадраты чётных чисел от 5 до 17",
    [x**2 for x in range(5, 17) if x % 2 == 0])