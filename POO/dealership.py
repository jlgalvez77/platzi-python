class Car:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            print(f'El automovil {self.brand} {self.model} ha sido alquilado')
        else:
            print(f'El automovil {self.brand} {self.model} no está disponible')

    def return_car(self):
        self.is_available = True
        print(f'El automovil {self.brand} {self.model} ha sido devuelto')


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_cars = []

    def rent_car(self, car):
        if car.is_available:
            self.is_available = False
            car.rent()
            self.rented_cars.append(car)
        else:
            print(f'El automovil {car.brand} {car.model} no está disponible')

    def return_car(self, car):
        if car in self.rented_cars:
            car.return_car()
            self.rented_cars.remove(car)
            print(f'El automovil {car.brand} {car.model} ha sido devuelto')
        else:
            print(f'El automovil {car.brand} {car.model} no está en tu lista de autos alquilados')


class CarRental:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'Automovil {car.brand} {car.model} agregado al concesionario')

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f'Cliente {customer.name} registrado en el concesionario')

    def show_available_cars(self):
        print('Automoviles disponibles:')
        for car in self.cars:
            if car.is_available:
                print(f'{car.brand} {car.model} {car.year} {car.color} ${car.price}')

# Crear los automoviles
car1 = Car('Toyota', 'Corolla', 2020, 'Rojo', 20000)
car2 = Car('Honda', 'Civic', 2019, 'Azul', 25000)
car3 = Car('Ford', 'Fiesta', 2018, 'Blanco', 18000)

# Crear los clientes
customer1 = Customer('Juan', 1)
customer2 = Customer('Karla', 2)

# Crear el concesionario
car_rental = CarRental()

# Agregar los automoviles al concesionario
car_rental.add_car(car1)
car_rental.add_car(car2)
car_rental.add_car(car3)

# Registrar los clientes en el concesionario
car_rental.register_customer(customer1)
car_rental.register_customer(customer2)

# Mostrar los automoviles disponibles
car_rental.show_available_cars()

# Alquilar un automovil
customer1.rent_car(car1)
customer2.rent_car(car2)

# Mostrar los automoviles disponibles
car_rental.show_available_cars()