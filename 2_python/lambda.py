people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Raveclaw"},
    {"name": "Draco", "house": "Slytherine"},
]


def f(person):
    return person["house"]


people.sort(key=lambda person: person["name"])
print(people)
