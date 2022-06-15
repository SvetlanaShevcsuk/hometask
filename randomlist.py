from random import randint

def randomlist(a = int(input("Начало диапазона:")), b = int(input("Конец диапазона:")), c = int(input("Количество элементов:"))):
    t = [randint(a, b) for i in range(c)]
    print(t)

randomlist()