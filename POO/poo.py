class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola, mi nombre es {self.name} y tengo {self.age} años')

person1 = Person('Juan', 28)
person2 = Person('Karla', 25)

person1.greet()
person2.greet()