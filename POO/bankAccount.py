class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo actual: {self.balance}')
        else:
            print('La cuenta está inactiva')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. Saldo actual: {self.balance}')
            else:
                print('Fondos insuficientes')
        else:
            print('La cuenta está inactiva')
    
    def deactivate(self):
        self.is_active = False
        print('Cuenta desactivada')

    def activate(self):
        self.is_active = True
        print('Cuenta activada')
            

account1 = BankAccount('Juan', 1000)
account2 = BankAccount('Karla', 2000)

# Llamadas a métodos
account1.deposit(500)
account1.withdraw(200)
account1.deactivate()
account1.deposit(1000)