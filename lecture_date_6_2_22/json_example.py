import json

x = {'avihay': 5, 'roy': 9, 'Ethan': 3, 'pegasus': 'Bla Bla'}
x['lst']=[1,2,3,'AEfawef',True]
with open('bla.json', 'w') as file:
    json.dump(x, file)
