numbers = {1: 'one', 2: 'two', 3: 'three'}
print(numbers[2])
information = {'name':'Jose',
               'last_name':'Galvez',
               'heigth':1.8,
               'age': 47}
print(information)
del information['age']
print(information)
llavez = information.keys()
print(llavez)
print(type(llavez))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {'Jose':{'last_name':'Galvez','heigth':1.8,'age': 47},
'Juan':{'last_name':'Perez','heigth':1.7,'age': 35}}
print(contacts)
print(contacts['Jose'])