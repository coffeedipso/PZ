#Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
#который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
#Пол: пол".
import pickle

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

class Figure:
    def calculate_area(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        return self.side_length ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

person1 = Person("Анна", 25, "женский")
person2 = Person("Иван", 30, "мужской")
person3 = Person("Мария", 35, "женский")
#Создайте класс "Фигура", который содержит метод расчета площади фигуры.
#Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
#"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
def save_def(person, filename):
    with open(filename, 'wb') as file:
        pickle.dump(person, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        person = pickle.load(file)
        return person

save_def(person1, "person1.pickle")
save_def(person2, "person2.pickle")
save_def(person3, "person3.pickle")

loaded_person1 = load_def("person1.pickle")
loaded_person2 = load_def("person2.pickle")
loaded_person3 = load_def("person3.pickle")

print(loaded_person1)
print(loaded_person2)
print(loaded_person3)

square = Square(5)
print("Площадь квадрата:", square.calculate_area())

rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.calculate_area())


#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате.

