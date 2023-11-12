# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)
def find_min_max_height(persons_dict):
    try:
        if not persons_dict:
            raise ValueError("Словарь пуст")
        
        min_height = float('inf') 
        max_height = float('-inf')  
        
        for person, height in persons_dict.items():
            if height < min_height:
                min_height = height
            if height > max_height:
                max_height = height
        
        return min_height, max_height
    
    except ValueError as e:
        print(f"Ошибка: {e}")

# Пример
persons = {"Андрей": 178, "Виктор": 150, "Максим": 200}
min_height, max_height = find_min_max_height(persons)
print(f"Наименьшая высота: {min_height}")
print(f"Наибольшая высота: {max_height}")