import itertools
def getAllCombinations(n, m):
    try:
        return [comb for comb in itertools.combinations(n, m)]
    except TypeError as e:
        print("Ошибка в типе аргумента (1 аргумент должен быть списком, а 2 целым числом)")