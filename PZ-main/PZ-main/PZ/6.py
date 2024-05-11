
# 1. Дан список размера N (N — четное число). Поменять местами первую и вторую
# половины списка.

def swap_halves(lst):
    try:
        if len(lst) % 2 != 0:
            raise ValueError("Размер списка должен быть четным числом.")
        
        midpoint = len(lst) // 2
        lst[:midpoint], lst[midpoint:] = lst[midpoint:], lst[:midpoint]
        return lst
    except ValueError as e:
        print(f"Ошибка: {e}")

#Пример
print(swap_halves([3,2,4,5]))

# 2. Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен среднему арифметическому элементов
# списка A с номерами от K до N.

def calculate_average(lst):
    try:
        if len(lst) == 0:
            raise ValueError("Список не должен быть пустым.")
        
        avg_lst = []
        for k in range(len(lst)):
            avg = sum(lst[k:]) / len(lst[k:])
            avg_lst.append(avg)
        
        return avg_lst
    except ValueError as e:
        print(f"Ошибка: {e}")

#Пример
print(calculate_average([3,2,4,5]))

# 3. Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
# A1, а исходное значение K первых элементов будет потеряно). Последние K
# элементов полученного списка положить равными 0.        

def shift_and_fill_zeros(lst, k):
    try:
        if len(lst) < 2 or k <= 1 or k >= len(lst):
            raise ValueError("Некорректное значение K.")
        
        shifted_lst = lst[k:] + [0] * k
        return shifted_lst
    except ValueError as e:
        print(f"Ошибка: {e}")

print(shift_and_fill_zeros([3,2,4,5],2))        