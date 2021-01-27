# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randrange

def filter_list(*args):

    yield [args[i + 1] for i in range(len(args) - 1) if args[i + 1] > args[i]]

    # result = []
    # for i in range(len(args)-1):
    #     if args[i + 1] > args[i]:
    #         result.append(args[i + 1])
    #         yield args[i + 1]



rand_list = [randrange(101) for el in range(25)]
new_list = list(filter_list(*rand_list))
print(f"Исходный список: {rand_list}\nРезультат: {new_list}")

