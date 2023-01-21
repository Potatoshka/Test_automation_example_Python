import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )


def generated_file():
    path = rf'C:\Users\potat\PycharmProjects\pythonProject3\test{random.randint(1, 99)}.txt'
    file = open(path, 'w')
    file.write(f'Hi,{random.randint(0, 100)}')
    file.close()
    return path
