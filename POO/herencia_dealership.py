class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehículo {self.brand} {self.model} ha sido vendido')
        else:
            print(f'El vehículo {self.brand} {self.model} no está disponible')
    
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError('Este método debe ser implementado en la subclase')
    
    def stop_engine(self):
        raise NotImplementedError('Este método debe ser implementado en la subclase')
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El vehículo {self.brand} {self.model} no está disponible'
        else:
            return f'El vehículo {self.brand} {self.model} está en marcha'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del vehículo {self.brand} {self.model} se ha detenido'
        else:
            return f'El vehículo {self.brand} {self.model} no está disponible'
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.brand} {self.model} no está disponible'
        else:
            return f'La bicicleta {self.brand} {self.model} está en marcha'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor de la bicicleta {self.brand} {self.model} se ha detenido'
        else:
            return f'La bicicleta {self.brand} {self.model} no está disponible'

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El camión {self.brand} {self.model} no está disponible'
        else:
            return f'El camión {self.brand} {self.model} está en marcha'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del camión {self.brand} {self.model} se ha detenido'
        else:
            return f'El camión {self.brand} {self.model} no está disponible'
        

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchuased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchuased_vehicles.append(vehicle)
        else:
            print(f'El vehículo {vehicle.brand} {vehicle.model} no está disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            available = 'Disponible'
        else:
            available = 'No disponible'
        print(f'{vehicle.brand} {vehicle.model} - Precio: {vehicle.get_price()} - {available}')
        
class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f'{vehicle.brand} {vehicle.model} agregado al concesionario')

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f'El cliente {customer.name} registrado en el concesionario')

    def show_available_vehicles(self):
        print('Vehículos disponibles:')
        for vehicle in self.vehicles:
            if vehicle.check_available():
                print(f'{vehicle.brand} {vehicle.model} - Precio: {vehicle.get_price()}')
    

car1 = Car('Toyota', 'Corolla', 20000)
bike1 = Bike('Trek', 'X-Caliber', 500)
truck1 = Truck('Ford', 'F-150', 30000)

customer1 = Customer('Juan')
customer2 = Customer('Karla')

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

# Mostrar vehículos disponibles
dealership.show_available_vehicles()

# Cliente consulta vehículo
customer1.inquire_vehicle(car1)

# Cliente compra vehículo
customer1.buy_vehicle(car1)

# Mostrar vehículos disponibles
dealership.show_available_vehicles()