import json

my_input = """
{
    "date": "2022-03-27",
    "number": 2344,
    "patient": {
        "name": "John Doe",
        "age": 18,
        "address": {
            "street": "Dallas Pkwy",
            "city": "Celina",
            "zipcode": 75009
        },
        "cars": [{"model":"GMC", "color":"red"}, {"model":"Ford", "color":"blue"}]
    }
}
"""


class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Patient:
    def __init__(self, name, age, address, cars):
        self.name = name
        self.age = age
        self.address = address
        self.cars = cars

class Claim:
    def __init__(self, date, number, patient):
        self.name = date
        self.number = number
        self.patient = patient

def hook(obj):
    obj_to_return = obj
    if "street" in obj:
        obj_to_return = Address(obj['street'], obj['city'], obj['zipcode'])
    elif "model" in obj:
        obj_to_return = Car(obj['model'], obj['color'])
    elif "age" in obj:
        obj_to_return = Patient(obj['name'], obj['age'], obj['address'], obj['cars'])
    elif "date" in obj:
        obj_to_return = Claim(obj['date'], obj['number'], obj['patient'])
    return obj_to_return

print('-----------')
data = json.loads(my_input, object_hook=hook)
print(data)

# class Presentation
# def __iter__(self):
#     yield from {
#         "street": self.street,
#         "city": self.city,
#         "zipcode": self.zipcode
#     }.items()
#
# def __str__(self):
#     return json.dumps(dict(self), ensure_ascii=False)
#
# def __repr__(self):
#     return self.__str__()
#
# def from_json(json_dct):
#     return Claim(json_dct['street'],
#                  json_dct['city'],
#                  json_dct['zipcode'])

# clear()	
# copy()	
# fromkeys()	
# get()	
# items()
# keys()
# pop()
# popitem()	
# setdefault()	
# update()
# values()



# from collections.abc import MutableMapping

# def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
#     items = []
#     for k, v in d.items():
#         new_key = parent_key + sep + k if parent_key else k
#         if isinstance(v, MutableMapping):
#             items.extend(flatten_dict(v, new_key, sep=sep).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)


# >>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
# {'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}



