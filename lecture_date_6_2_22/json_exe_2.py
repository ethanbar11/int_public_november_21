import json


class Dog:
    def __init__(self, name, age, dog_type, loves_cats):
        self.loves_cats = loves_cats
        self.dog_type = dog_type
        self.age = age
        self.name = name

    def __str__(self):
        return 'My name is {} and my age is {} my type is {} and I love cats :{}'.format(self.name, self.age
                                                                                         , self.dog_type,
                                                                                         self.loves_cats)


def json_to_dog(path):
    with open(path, 'r') as json_file:
        data_dict = json.load(json_file)
        name = data_dict['name']
        age = data_dict['age']
        dog_type = data_dict['dog_type']
        loves_cats = data_dict['loves_cats']
        dog = Dog(name, age, dog_type, loves_cats)
        return dog


if __name__ == '__main__':
    # dog = Dog('doggy', 28, 'Labrador', False)
    #
    # # json.dumps receives an object that can be serialized (converted) to json
    # # and returns a json string.
    # json_str = json.dumps(dog.__dict__)
    # with open('exe_3.json', 'w') as file:
    #     file.write(json_str)
    #
    # # Second alternative
    # with open('exe_3.json', 'w') as file:
    #     json.dump(dog.__dict__, file)

    dog = json_to_dog('exe_3.json')
    print(dog)
