"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
count_num = 0  # создаем счетчик
res_sum = 0   # сюда будем складывать результат
a = 1         # наше число которое нам нужно делить а потом складывать
n = int(input("Введите число "))


def my_func(a):
    global count_num, res_sum
    if count_num == n:  # Базовый случай
        return res_sum

    count_num += 1        # Счетчик
    res_sum = res_sum + a   # сохранение результата
    return my_func((a * -1)/2)


res = my_func(a)
print(res)
