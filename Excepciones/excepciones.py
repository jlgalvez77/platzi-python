try:
    divisor = int(input("Introduce un número divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("No se puede dividir por cero")
    print(f'Ha ocurrido un error: {e}')
except ValueError as e:
    print(f'Ha ocurrido un error: {e}')
    print("Debes introducir un número")