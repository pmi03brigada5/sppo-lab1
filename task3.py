# 3 Задание
print("")
print("Функция и лямба Функция:")
def calculateFibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)
print(calculateFibonacci(10)) # output: 34

fibonacci = lambda n: 0 if n == 1 else 1 if n == 2 else fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) # output: 34