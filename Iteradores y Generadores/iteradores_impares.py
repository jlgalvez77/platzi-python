# Crear un iterador para los numeros impares

# Limite
limit = 10
# Crear un iterador para los numeros impares
odd_itter = iter(range(1, limit+1, 2))
# Usar el iterador
for num in odd_itter:
    print(num)