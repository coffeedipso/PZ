A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (>0): "))

sum = 1  # инициализируем сумму

for i in range(1, N+1):
    sum += A ** i

print("Сумма ряда: ", sum)



try:
    N = int(input("Введите целое число N (> 0): "))
    reversed_num = 0
    original_num = N

    while N > 0:
        digit = N % 10
        reversed_num = reversed_num * 10 + digit
        N = N // 10

    print("Число", original_num, "прочитанное справа налево:", reversed_num)

except ValueError:
    print("Ошибка: введено некорректное значение.")
