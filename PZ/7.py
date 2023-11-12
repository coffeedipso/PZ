# 1. Даны строки S и S0. Удалить из строки S последнюю подстроку, совпадающую с S0.
# Если совпадающих подстрок нет, то вывести строку S без изменений.

def remove_last_substring(s, s0):
    try:
        if len(s0) == 0:
            raise ValueError("Строка S0 не должна быть пустой.")
        
        if s.endswith(s0):
            return s[:len(s) - len(s0)]
        else:
            return s
    except ValueError as e:
        print(f"Ошибка: {e}")

print(remove_last_substring("Remove string", "string"))


# 2. Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Найти количество слов, которые
# содержат хотя бы одну букву «А».

def count_words_with_a(s):
    try:
        words = s.split()
        count = 0
        for word in words:
            if 'a' in word or 'A' in word:
                count += 1
        
        return count
    except ValueError as e:
        print(f"Ошибка: {e}")

print(count_words_with_a("Banana Apple rock"))