# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

if len(argv) != 4:
    exit(print("Введите 3 параметра при запуске скрипта: количество отработанных часов, размер почасовой оплаты, \n"
               "и размер премии (если сотрудник отработал более 40 часов).\n"))

for i in range(1, 4):
    while True:
        try:
            argv[i] = float(argv[i])
            if argv[i] < 0:
                argv[i] = abs(argv[i])   #здесь отрицательных чисел у нас быть не может
                continue
        except ValueError:
            argv[i] = input(f"Вместо {argv[i]} нужно ввести число.\n")
            continue
        break

script_name, work_hours, hour_rate, bonus = argv

print(f"Сотрутник отработал {work_hours} ч.")
print(f"Почасовая ставка сотрудника равна {hour_rate} руб.")

if work_hours > 40:
    print(f"Сотрутник отработал более 40 часов. Зарплата с премией составляет {work_hours * hour_rate + bonus} руб.")
else:
    print(f"Сотрутник отработал менее 40 часов. Зарплата без премии составляет {work_hours * hour_rate} руб.")


