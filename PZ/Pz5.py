# 1. Составить функцию, которая выведет на экран строку, содержащую задаваемое с
# клавиатуры число символов.


def show_string_with_character_count():
    try:
        count = int(input("Введите количество символов: "))  # Вводим количество символов с клавиатуры и преобразуем его в целое число
        if count < 0:
            raise ValueError("Количество символов должно быть неотрицательным")

        string = "#" * count  # Создаем строку, содержащую заданное количество символов "#"
        print("Строка с", count, "символами:", string)

    except ValueError as ve:
        print("Ошибка ввода:", ve)
    except Exception as e:
        print("Произошла ошибка:", e)

show_string_with_character_count()

# 2. Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
# значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить правый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).


def shift_right_3(a, b, c):
    temp = a
    a = c
    c = b
    b = temp
    return a, b, c

try:
    a1, b1, c1 = input("Введите три числа через пробел для первого набора: ").split()
    a1 = float(a1)
    b1 = float(b1)
    c1 = float(c1)
    shifted_a1, shifted_b1, shifted_c1 = shift_right_3(a1, b1, c1)
    print(f"Результат сдвига первого набора: {shifted_a1}, {shifted_b1}, {shifted_c1}")

    a2, b2, c2 = input("Введите три числа через пробел для второго набора: ").split()
    a2 = float(a2)
    b2 = float(b2)
    c2 = float(c2)
    shifted_a2, shifted_b2, shifted_c2 = shift_right_3(a2, b2, c2)
    print(f"Результат сдвига второго набора: {shifted_a2}, {shifted_b2}, {shifted_c2}")
except ValueError:
    print("Ошибка: Введены некорректные данные чисел.")