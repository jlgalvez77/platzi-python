numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(f'El valor de i es: {i}')

for i in range(10):
    print(f'El valor de i es: {i}')

fruits = ['manzana', 'pera', 'mango', 'uva', 'naranja']
for fruit in fruits:
    print(fruit)
    if fruit == 'naranja':
        print('Naranja encontrada')

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i == 3:
        continue
    print(f'El valor de i es: {i}')