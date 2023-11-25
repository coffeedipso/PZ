a = int(input("Введите значение стороны a: "))
b = 6
c = int(input("Введите значение стороны c: "))

if a == c:
    print(f"Треугольник со сторонами {a}, {b}, {c} является равнобедренным")
else:
    print(f"Треугольник со сторонами {a}, {b}, {c} не является равнобедренным")







num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
max_num = max(num1, num2, num3)
if num1 == max_num:
    sum_of_max = num1 + max(num2, num3)
elif num2 == max_num:
    sum_of_max = num2 + max(num1, num3)
else:
    sum_of_max = num3 + max(num1, num2)

print("Сумма двух наибольших чисел:", sum_of_max)

