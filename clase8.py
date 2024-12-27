to_do = ['Ir al  hotel',
         'Ir a la playa',
         'Ir a comer',
         'Ir a la piscina',
         'Volver al hotel',]
print(to_do)
numbers = [1, 2, 3, 4, 'cinco']
print(numbers)
print(type(numbers))
mix = ['uno', 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print(f'Primer elemento de la lista: {mix[0]}')
print(f'Último elemento de la lista: {mix[-1]}')

string = 'Hola mundo'
print(mix[0:2])

print(mix)
mix.append(False)
print(mix)
mix.append(['a', 'b', 'c'])
print(mix)
mix.insert(1, 'dos')
print(mix)
print(mix.index(3.14))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Número mayor:', max(numbers))
print('Número menor:', min(numbers))
print('Suma de los números:', sum(numbers))
del numbers[0]
print(numbers)
del numbers
# print(numbers) Produce un error debido a que la lista fue eliminada