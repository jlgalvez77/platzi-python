class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola, mi nombre es {self.name} y tengo {self.age} años')

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        super().greet()
        print(f'Mi número de estudiante es {self.student_id}')


student = Student('Juan', 28, 'A0123')
student.greet()