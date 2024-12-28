class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print(f'El libro {self.title} no está disponible')

    def return_book(self):
        self.is_available = True
        print(f'El libro {self.title} ha sido devuelto')


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro {book.title} no está disponible')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro {book.title} no está en tu lista de libros prestados')	


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Libro {book.title} agregado a la biblioteca')

    def register_user(self, user):
        self.users.append(user)
        print(f'Usuario {user.name} registrado en la biblioteca')

    def show_available_books(self):
        print('Libros disponibles:')
        for book in self.books:
            if book.is_available:
                print(f'{book.title} por {book.author}')


# Crear los libros
book1 = Book('El principito', 'Antoine de Saint-Exupéry')
book2 = Book('El túnel', 'Ernesto Sábato')
book3 = Book('Cien años de soledad', 'Gabriel García Márquez')
# Crear los usuarios
user1 = User('Juan', 1)
user2 = User('Karla', 2)
# Crear la biblioteca
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

# Mostrar libros disponibles
library.show_available_books()

# Prestar un libro
user1.borrow_book(book1)

# Mostrar libros disponibles
library.show_available_books()

# Devolver un libro
user1.return_book(book1)

# Mostrar libros disponibles
library.show_available_books()