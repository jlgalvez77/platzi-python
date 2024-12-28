def greet(name, lastname = 'Doe'):
    print(f'Hello {name} {lastname}')

greet('José', 'Gálvez')
greet('David')
greet(lastname='Gálvez', name='José')