# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from random import randrange
from itertools import count
from itertools import cycle

print(f"Реализованы 2 скрипта:\nA) Итератор, генерирующий целые числа, начиная с указанного\nB) Итератор, повторяющий элементы некоторого списка, определенного заранее.")

def script(i):

    while True:
        try:
            i = int(i)
        except ValueError:
            i = input(f"Вместо {i} введите целое число.\n")
            continue
        break
    return i


user_answer = input("Какой скрипт будем выполнять A или B?\n").lower()
while True:
    if user_answer not in {"a", "b"}:
        user_answer = input("Ошибка ввода. Введите \"A\" или \"B\" .\n")
        continue
    break

if user_answer == "a":
    start_number = script(input("Введите начальное число последовательности?\n"))
    while True:
        step = script(input("Будем увеличивать (1) или уменьшать (-1) последующие числа?\n"))
        if step not in {-1, 1}:
            print("Ошибка. Попробуйте снова.")
            continue
        break

    while True:
        last_number = script(input("До какого числа будем выводить последовательность?\n"))
        if (step == 1 and last_number - start_number < 0) or \
                (step == -1 and last_number - start_number > 0) or start_number == last_number:
            print("Ошибка. Попробуйте снова.\n"
                  "В возрастающей последовательности это число должно быть больше начального.\n"
                  "Для убывающей последовательности это число должно быть меньше начального.\n"
                  "Также введенное число не должно быть равно изначальному.")
            continue
        break

    for element in count(start_number, step):
        if last_number - start_number > 0:
            if element > last_number:
                break
            else:
                print(element)
        else:
            if element < last_number:
                break
            else:
                print(element)

else:
    start_list = [randrange(101) for element in range(10)]
    print(f"Имеется следующий список:\n{start_list}\n")
    while True:
        last_number = script(input("Сколько раз повторить элементы из списка?\n"))
        if last_number <= 0:
            print("Ошибка ввода. Нужно положительное число.")
            continue
        break
    counter = 0
    for element in cycle(start_list):
        if counter >= last_number:
            break
        print(element)
        counter += 1


# Все условия выхода и выбора предоставим пользователю. Второе условие сформулировано не совсем понятно, но надеюсь я его правильно понял