# Gemeramos numeros pares
def evens():
    for num in range(100):
        if num % 2 == 0:
            yield num
# Imprimimos los numeros pares
for num in evens():
    print(num)
# Generamos numeros impares
def odds():
    for num in range(100):
        if num % 2 != 0:
            yield num
# Imprimimos los numeros impares
for num in odds():
    print