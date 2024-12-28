def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True:
        print('Selecciona una operación:')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')

        option = int(input('Ingresa una opción(1, 2, 3, 4, 5): '))

        if option == 5:
            print('Saliendo...')
            break
        if option < 1 or option > 5:
            print('Opción inválida')
            continue
        if option in [1, 2, 3, 4]:
            a = float(input('Ingresa el primer número: '))
            b = float(input('Ingresa el segundo número: '))
            if option == 1:
                print(f'{a} + {b} = {add(a, b)}')
            elif option == 2:
                print(f'{a} - {b} = {subtract(a, b)}')
            elif option == 3:
                print(f'{a} * {b} = {multiply(a, b)}')
            elif option == 4:
                print(f'{a} / {b} = {divide(a, b)}')

calculator()