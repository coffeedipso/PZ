# 1. Организовать и вывести последовательность на N произвольных целых элементов, 
# сформировать новую последовательность куда поместить отрицательные нечетные элементы, 
#найти их сумму и среднее арифметическое.
# 2. Из заданной строки отобразить только цифры. Использовать библиотеку string. 
# Строка - The Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230metres) long and 481 feet (147 metres) high.



#1

import random

N = 10
sequence = [random.randint(-100, 100) for _ in range(N)]
print("Последовательность:", sequence)

new_sequence = [x for x in sequence if x < 0 and x % 2 != 0]
print("Новая последовательность:", new_sequence)

sum_of_neg_odd = sum(new_sequence)
average_of_neg_odd = sum_of_neg_odd / len(new_sequence) if len(new_sequence) > 0 else 0
print("Сумма отрицательных нечетных элементов:", sum_of_neg_odd)
print("Среднее арифметическое отрицательных нечетных элементов:", average_of_neg_odd)

#2
import string

text = "The Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230metres) long and 481 feet (147 metres) high."

digits = ''.join(filter(lambda x: x in string.digits, text))
print("Только цифры из строки:", digits)
