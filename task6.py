# 6 Задание
print("")
print("Генератор фибоначи:")
def fibonaccis(n):
    currf, nextf, counter = 0, 1, 0 
    while True:
        if counter > n: return
        yield currf
        currf, nextf = nextf, currf + nextf
        counter += 1
fibonaccis = fibonaccis(5)
for i in fibonaccis:
    print(i)