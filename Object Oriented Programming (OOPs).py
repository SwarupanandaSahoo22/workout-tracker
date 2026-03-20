# Object Oriented Programming (OOPs)

# Object: A "bundel" of related attributes (variables) & methods (functions)
#         Ex. phone, cup, book
#         You need a class to create many projects

# Class: (blueprint) used to design the structure & layout of an object



# class Car:
#     def __init__(self, model, year, colour, for_sale):
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.for_sale = for_sale   

#     def drive(self):
#         print(f"You drive the {self.colour} {self.model}")
    
#     def stop(self):
#         print(f"You stop the {self.colour} {self.model}")

#     def describe(self):
#         print(f"{self.year} {self.colour} {self.model}")

# car1 = Car("Mustang", 2022, "red", True)
# car2 = Car("BMW", 2021, "black", False)
# car3 = Car("Mustang", 2023, "yellow", True)

# car1.describe()
# car2.describe()
# car3.describe()











# Class variable: Shared among all instances among class
#                 Defined outside the constuctor
#                 Allow you to share data among all objects created from that class


# class Student:

#     class_year = 2024
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student("Spongbob", 17)
# student2 = Student("Patrick", 16)
# student3 = Student("Sandy", 27)
# student4 = Student("Squidward", 44)
# student5 = Student("Plankton", 23)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students:")
# print()
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)
# print(student5.name)









# Inheritance: Allows a class to inherit attributes & methods from another class
#              Helps in code reuseability & expansibility
#              class Child(Parent)


# class Animals:

#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animals):
#     def speak(self):
#         print("WOOF!")
# class Cat(Animals):
#     def speak(self):
#         print("MEOW!")
# class Mouse(Animals):
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# cat.speak()











# super(): Functions used in a child class to call methods from a parent class (Super-function)
#          Allows you to extend the fuctionality of the inherited methods.

# class Shape:
#     def __init__(self, colour, is_filled):
#         self.colour = colour
#         self.is_filled = is_filled

# class Circle(Shape):
#     def __init__(self, colour, is_filled, radius):
#         super().__init__(colour, is_filled)
#         self.radius = radius

# class Square(Shape):
#     def __init__(self, colour, is_filled, width):
#         super().__init__(colour, is_filled)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, colour, is_filled, width, height):
#         super().__init__(colour, is_filled)
#         self.width = width
#         self.height = height

# circle = Circle(colour="Red", is_filled=True, radius=5)
# square = Square(colour="Green", is_filled=False, width=7)
# triangle = Triangle(colour="Blue", is_filled=True, width=4, height=8)

# print()
# print("========== circle ==========")
# print()

# print(circle.colour)
# print(f"{circle.radius}cm")
# print(circle.is_filled)

# print()
# print("========== square ==========")
# print()

# print(square.colour)
# print(f"{square.width}cm")
# print(square.is_filled)

# print()
# print("========== triangle ==========")
# print()

# print(triangle.colour)
# print(f"{triangle.width}cm & {triangle.height}cm")
# print(triangle.is_filled)
# print()









# Polymorphism: Greek word that means to "Have many forms or faces"
#               Poly = Many
#               Morph = Faces

#               TWO WAYS TO ACHIEVE POLYMORPHISM:
#               1. INHERITANCE: An object could be treated of the same type as the parent class

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2
    
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return 0.5 * self.base * self.height
    
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(4), Square(8), Triangle(9, 18), Pizza("Pepperonni", 8)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")








#              2. DUCK TYPING: "It it walks like a duck & quacks like a duck, it's a duck"

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(Self):
#         print("MEOW!")

# class Car:
#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()










# Static methods = A method that belong to a class rather than an object from that class (instance)
#                  Usually used for general utility funtions

# Instance methods = Best for operations on instance of the class (object)
# Static methods = Best for utility functions that do not need access to class data

# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_postion = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_postion
    
# employee1 = Employee("Eugune", "Manager")
# employee2 = Employee("Squidward", "Cashier")
# employee3 = Employee("Spongbob", "Cook")
# employee4 = Employee("Patrick", "Janitor")

# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())
# print(employee4.get_info())









# Class methods: Allows operations related to class itself
#                Take (cls) as the first parameter, which represents the class itself


# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     def get_info(self):
#         return f"{self.name} - {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total number of students: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
        
# student1 = Student("Spongbob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Spongbob", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())










# Magic method: Dunder method (double underscore) __init__, __str__, __eq__, etc.
#               They're automatically called by many Python's built-in operations.
#               They allow developers to define or customize the behaviour of objects.

class Books:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, total pages: {self.num_pages}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == self.title
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        

book1 = Books("The Alchemist", "Paulo Coelho", 208)
book2 = Books("The Silent Patient", "Alex Michaelides", 336)
book3 = Books("The Great Gatsby", "F.Scott Fitzgerald", 180)

print(book3)
print(book1 == book2)
print(book2 < book3)
print(book2 > book3)
print(book1 + book3)
print("Patient" in book2)
print(book1['pizza'])