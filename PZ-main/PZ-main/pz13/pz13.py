# 1. Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое. 
# 2. В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры). 

#1
matrix = [
    [1, 2, 3],
    [4, -5, 6],
    [7, 8, -9]
]

positive_even_elements = [x for row in matrix for x in row if x > 0 and x % 2 == 0]
print("Массив из положительных четных элементов матрицы:", positive_even_elements)

sum_of_positive_even = sum(positive_even_elements)
average_of_positive_even = sum_of_positive_even / len(positive_even_elements) if len(positive_even_elements) > 0 else 0
print("Сумма положительных четных элементов:", sum_of_positive_even)
print("Среднее арифметическое положительных четных элементов:", average_of_positive_even)

#2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = int(input("Введите номер столбца N: "))

column = [row[N-1] for row in matrix]
sum_of_column = sum(column)
product_of_column = 1
for element in column:
    product_of_column *= element

print("Сумма элементов столбца N:", sum_of_column)
print("Произведение элементов столбца N:", product_of_column)
