square = [x**2 for x in range(10)]
#print(f'Los cuadrados son: {square}')

celsius = [0, 10, 20.1, 34.5]
fahrenheight =[(temp * 9/5) + 32 for temp in celsius]
#print(f'Los grados fahrenheight son: {fahrenheight}')

# Numeros pares
evens = [x for x in range(21) if x % 2 == 0]
#print(f'Los numeros pares son: {evens}')

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transpose)