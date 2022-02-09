import json
lst = []
for i in range(1, 21):
    lst.append(i)

dic = {'lst': lst,
       'name': 'Ethan', 'last name': 'Bar'}

with open('blabla.json','w') as file:
    json.dump(dic,file,indent=1)